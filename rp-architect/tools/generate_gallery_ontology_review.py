#!/usr/bin/env python3
"""Generate compact human/LLM review views from Gallery's canonical RP ontology snapshot.

The snapshot remains the source of truth. These outputs are deterministic projections
and must not introduce semantic categories, aliases, descriptions, or RP policy that
is absent from the snapshot.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_snapshot(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_snapshot(s: dict[str, Any]) -> dict[int, dict[str, Any]]:
    tags = s["tags"]
    edges = s["hierarchy_edges"]
    counts = s["entity_counts"]

    if len(tags) != counts["tags"]:
        raise ValueError("Tag count mismatch")

    by_id = {t["tag_id"]: t for t in tags}
    if len(by_id) != len(tags):
        raise ValueError("Duplicate tag_id")

    seen_names: set[str] = set()
    for t in tags:
        key = t["name"].lower()
        if key in seen_names:
            raise ValueError(f"Duplicate tag name (case-insensitive): {t['name']}")
        seen_names.add(key)

        for p in t.get("parent_ids", []):
            if p not in by_id:
                raise ValueError(f"Missing parent {p} for {t['tag_id']}")
        for c in t.get("child_ids", []):
            if c not in by_id:
                raise ValueError(f"Missing child {c} for {t['tag_id']}")

    edge_set: set[tuple[int, int]] = set()
    for e in edges:
        key = (e["child_tag_id"], e["parent_tag_id"])
        if key in edge_set:
            raise ValueError(f"Duplicate hierarchy edge {key}")
        edge_set.add(key)

    if len(edge_set) != counts["hierarchy_edges"]:
        raise ValueError("Hierarchy edge count mismatch")

    parent_derived: set[tuple[int, int]] = set()
    for t in tags:
        tid = t["tag_id"]
        for p in t.get("parent_ids", []):
            parent_derived.add((tid, p))
            if tid not in by_id[p].get("child_ids", []):
                raise ValueError(f"Non-reciprocal parent relation {(tid, p)}")
        for c in t.get("child_ids", []):
            if tid not in by_id[c].get("parent_ids", []):
                raise ValueError(f"Non-reciprocal child relation {(c, tid)}")

    if parent_derived != edge_set:
        raise ValueError("hierarchy_edges differ from tag parent_ids")

    state: dict[int, int] = {}

    def visit(tag_id: int) -> None:
        st = state.get(tag_id, 0)
        if st == 1:
            raise ValueError(f"Hierarchy cycle detected at {tag_id}")
        if st == 2:
            return
        state[tag_id] = 1
        for child_id in by_id[tag_id].get("child_ids", []):
            visit(child_id)
        state[tag_id] = 2

    for tag_id in by_id:
        visit(tag_id)

    exposed = sum(1 for t in tags if t["roleplay_exposed"])
    overrides = sum(1 for t in tags if t["roleplay_priority"]["overridden"])
    if exposed != counts["roleplay_exposed_tags"]:
        raise ValueError("RP exposed count mismatch")
    if overrides != counts["priority_overrides"]:
        raise ValueError("Priority override count mismatch")

    return by_id


def build_review(s: dict[str, Any], by_id: dict[int, dict[str, Any]]) -> dict[str, Any]:
    def name(tag_id: int) -> str:
        return by_id[tag_id]["name"]

    def compact(t: dict[str, Any]) -> dict[str, Any]:
        return {
            "id": t["tag_id"],
            "name": t["name"],
            "rp": bool(t["roleplay_exposed"]),
            "counts": {
                "canonical": t["counts"]["canonical_unique_contents"],
                "direct": t["counts"]["direct_source_unique_contents"],
                "inherited": t["counts"]["inherited_source_unique_contents"],
            },
            "priority": t["roleplay_priority"]["effective"],
            "parents": [name(x) for x in t.get("parent_ids", [])],
            "children": [name(x) for x in t.get("child_ids", [])],
        }

    tags = sorted(s["tags"], key=lambda t: t["tag_id"])
    roots = [t for t in tags if not t.get("parent_ids")]
    exposed = [t for t in tags if t["roleplay_exposed"]]
    hidden = [t for t in tags if not t["roleplay_exposed"]]
    hidden_with_content = [t for t in hidden if t["counts"]["canonical_unique_contents"] > 0]
    exposed_zero = [t for t in exposed if t["counts"]["canonical_unique_contents"] == 0]

    def short_index(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return [
            {
                "id": t["tag_id"],
                "name": t["name"],
                "canonical": t["counts"]["canonical_unique_contents"],
                "priority": t["roleplay_priority"]["effective"],
            }
            for t in items
        ]

    return {
        "schema_version": "gallery-rp-ontology-review/v1",
        "generated_from": {
            "snapshot_file": "gallery_rp_ontology_snapshot.json",
            "snapshot_schema_version": s["schema_version"],
            "snapshot_exported_at": s["exported_at"],
            "gallery_commit": s["gallery_commit"],
        },
        "summary": {
            "tags": len(tags),
            "roleplay_exposed_tags": len(exposed),
            "roleplay_hidden_tags": len(hidden),
            "hierarchy_edges": len(s["hierarchy_edges"]),
            "priority_overrides": s["entity_counts"]["priority_overrides"],
            "roots": len(roots),
            "roleplay_hidden_with_content": len(hidden_with_content),
            "roleplay_exposed_zero_canonical": len(exposed_zero),
        },
        "source_scope": s["source"],
        "semantics": s["semantics"],
        "unavailable": s["unavailable"],
        "warnings": s["warnings"],
        "indexes": {
            "roots": short_index(roots),
            "roleplay_exposed": short_index(exposed),
            "roleplay_hidden_with_content": short_index(hidden_with_content),
            "roleplay_exposed_zero_canonical": short_index(exposed_zero),
        },
        "tags": [compact(t) for t in tags],
    }


def build_markdown(s: dict[str, Any], by_id: dict[int, dict[str, Any]]) -> str:
    tags = sorted(s["tags"], key=lambda t: t["tag_id"])
    roots = [t for t in tags if not t.get("parent_ids")]
    exposed = [t for t in tags if t["roleplay_exposed"]]
    hidden = [t for t in tags if not t["roleplay_exposed"]]
    hidden_with_content = [t for t in hidden if t["counts"]["canonical_unique_contents"] > 0]
    exposed_zero = [t for t in exposed if t["counts"]["canonical_unique_contents"] == 0]

    def name(tag_id: int) -> str:
        return by_id[tag_id]["name"]

    def fmt(t: dict[str, Any]) -> str:
        rp = "RP ✓" if t["roleplay_exposed"] else "RP hidden"
        c = t["counts"]["canonical_unique_contents"]
        d = t["counts"]["direct_source_unique_contents"]
        i = t["counts"]["inherited_source_unique_contents"]
        p = t["roleplay_priority"]["effective"]
        return f"{t['name']} [{rp}; c={c}; d={d}; i={i}; priority={p}]"

    def esc(value: str) -> str:
        return value.replace("|", "\\|")

    lines: list[str] = [
        "# Gallery RP Ontology Review",
        "",
        "> GENERATED FILE. Do not edit manually. Regenerate from `gallery_rp_ontology_snapshot.json` with `tools/generate_gallery_ontology_review.py`.",
        "",
        "## Source",
        "",
        f"- Snapshot schema: `{s['schema_version']}`",
        f"- Snapshot exported at: `{s['exported_at']}`",
        f"- Gallery commit: `{s['gallery_commit']}`",
        f"- Source kind: `{s['source']['kind']}`",
        f"- Source scope: `{s['source']['scope']}`",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
        f"| Tags | {len(tags)} |",
        f"| RP exposed | {len(exposed)} |",
        f"| RP hidden | {len(hidden)} |",
        f"| Hierarchy edges | {len(s['hierarchy_edges'])} |",
        f"| Priority overrides | {s['entity_counts']['priority_overrides']} |",
        f"| Root tags | {len(roots)} |",
        f"| RP hidden with canonical content | {len(hidden_with_content)} |",
        f"| RP exposed with canonical count 0 | {len(exposed_zero)} |",
        "",
        "## Reading notes",
        "",
        "- `c` = canonical unique contents. This includes materialized inherited tags.",
        "- `d` = direct-source unique contents.",
        "- `i` = inherited-source unique contents.",
        "- Direct and inherited source counts can overlap and are not a partition.",
        "- Hierarchy is immediate child → parent semantics. It does not imply RP exposure.",
        "- RP exposure is an explicit stored flag, independent of hierarchy.",
        "- Priority shown here is the effective per-tag RP priority. It does not inherit through hierarchy.",
        "- This review does not invent categories, aliases, descriptions, RP domains, or other semantics absent from the snapshot.",
        "",
        "## Hierarchy by root",
        "",
        "Multi-parent tags are intentionally repeated under each applicable root path.",
        "",
    ]

    def render_node(tag_id: int, depth: int, path: set[int]) -> None:
        if tag_id in path:
            raise ValueError(f"Cycle while rendering {tag_id}")
        t = by_id[tag_id]
        multi = (
            "; parents=" + " | ".join(name(x) for x in t.get("parent_ids", []))
            if len(t.get("parent_ids", [])) > 1
            else ""
        )
        lines.append("  " * depth + "- " + fmt(t) + multi)
        next_path = set(path)
        next_path.add(tag_id)
        for child_id in sorted(t.get("child_ids", [])):
            render_node(child_id, depth + 1, next_path)

    for root in [t for t in roots if t.get("child_ids")]:
        lines += [f"### {root['name']}", ""]
        render_node(root["tag_id"], 0, set())
        lines.append("")

    lines += [
        "## Standalone root tags",
        "",
        "| ID | Tag | RP | Canonical | Direct | Inherited | Priority |",
        "| ---: | --- | :---: | ---: | ---: | ---: | ---: |",
    ]
    for t in [x for x in roots if not x.get("child_ids")]:
        lines.append(
            f"| {t['tag_id']} | {esc(t['name'])} | {'✓' if t['roleplay_exposed'] else ''} | "
            f"{t['counts']['canonical_unique_contents']} | {t['counts']['direct_source_unique_contents']} | "
            f"{t['counts']['inherited_source_unique_contents']} | {t['roleplay_priority']['effective']} |"
        )
    lines += ["", "## RP-exposed vocabulary", "", "| ID | Tag | Canonical | Direct | Inherited | Priority | Parents |",
              "| ---: | --- | ---: | ---: | ---: | ---: | --- |"]
    for t in exposed:
        parents = esc(", ".join(name(x) for x in t.get("parent_ids", [])))
        lines.append(
            f"| {t['tag_id']} | {esc(t['name'])} | {t['counts']['canonical_unique_contents']} | "
            f"{t['counts']['direct_source_unique_contents']} | {t['counts']['inherited_source_unique_contents']} | "
            f"{t['roleplay_priority']['effective']} | {parents} |"
        )

    lines += [
        "",
        "## RP-hidden tags with canonical content",
        "",
        "These are review candidates only. Presence here does not mean they should be exposed.",
        "",
        "| ID | Tag | Canonical | Direct | Inherited | Parents |",
        "| ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for t in hidden_with_content:
        parents = esc(", ".join(name(x) for x in t.get("parent_ids", [])))
        lines.append(
            f"| {t['tag_id']} | {esc(t['name'])} | {t['counts']['canonical_unique_contents']} | "
            f"{t['counts']['direct_source_unique_contents']} | {t['counts']['inherited_source_unique_contents']} | {parents} |"
        )

    lines += [
        "",
        "## RP-exposed tags with canonical count 0",
        "",
        "A zero snapshot count does not prove that the tag cannot return anything from Gallery's complete hybrid retrieval pool.",
        "",
        "| ID | Tag | Priority | Parents |",
        "| ---: | --- | ---: | --- |",
    ]
    for t in exposed_zero:
        parents = esc(", ".join(name(x) for x in t.get("parent_ids", [])))
        lines.append(f"| {t['tag_id']} | {esc(t['name'])} | {t['roleplay_priority']['effective']} | {parents} |")

    lines += ["", "## Snapshot-declared unavailable semantics", ""]
    for item in s.get("unavailable", []):
        lines.append(f"- {item}")
    lines.append("")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "snapshot",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "gallery_rp_ontology_snapshot.json",
    )
    parser.add_argument(
        "--json-out",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "gallery_rp_ontology_review.json",
    )
    parser.add_argument(
        "--md-out",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "gallery_rp_ontology_review.md",
    )
    args = parser.parse_args()

    snapshot = load_snapshot(args.snapshot)
    by_id = validate_snapshot(snapshot)
    review = build_review(snapshot, by_id)
    markdown = build_markdown(snapshot, by_id)

    args.json_out.write_text(
        json.dumps(review, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    args.md_out.write_text(markdown, encoding="utf-8")

    print(f"Wrote {args.json_out}")
    print(f"Wrote {args.md_out}")


if __name__ == "__main__":
    main()
