"""Initialize a new novel project from the skill's template.

Default behavior is idempotent: missing files/dirs are created, existing files
are left untouched. Use --force to overwrite, --dry-run to preview.
"""
import argparse
import shutil
import sys
from pathlib import Path


def iter_template_files(template_dir: Path):
    """Yield (relative_path, source_path) for every file in the template."""
    for src in template_dir.rglob("*"):
        if src.is_file():
            yield src.relative_to(template_dir), src


def init_novel(target_path: str, force: bool = False, dry_run: bool = False) -> bool:
    target_dir = Path(target_path).resolve()
    script_dir = Path(__file__).parent
    skill_dir = script_dir.parent
    template_dir = skill_dir / "assets" / "template"

    if not template_dir.exists():
        print(f"[error] Template directory not found at {template_dir}")
        return False

    mode = "[dry-run] " if dry_run else ""
    print(f"{mode}Initializing novel project at: {target_dir}")
    print(f"{mode}Template source: {template_dir}\n")

    created, skipped, overwritten = [], [], []

    for rel, src in iter_template_files(template_dir):
        dst = target_dir / rel
        if dst.exists():
            if force:
                overwritten.append(rel)
                if not dry_run:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
            else:
                skipped.append(rel)
        else:
            created.append(rel)
            if not dry_run:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)

    for rel in created:
        print(f"  [create] {rel}")
    for rel in overwritten:
        print(f"  [overwrite] {rel}")
    for rel in skipped:
        print(f"  [skip] {rel} (exists; use --force to overwrite)")

    print(
        f"\n{mode}Done. created={len(created)} overwritten={len(overwritten)} skipped={len(skipped)}"
    )

    if not dry_run and (created or overwritten):
        print("\nRecommended next steps:")
        print(f"  1. cd {target_dir}")
        print("  2. Fill plans/global_plan.md (logline, core conflict, three-act arc, chapter index).")
        print("  3. Fill plans/setting/characters.md and plans/setting/world.md.")
        print("  4. Fill plans/chapters/ch01_plan.md with your first chapter outline.")
        print("  5. Add style samples to references/ (NOT the skill's docs/).")
        print("  6. Edit feedback/requirements.md: remove placeholders, add project-specific rules.")
        print("  7. (Optional) Review config/instruction.md — SillyTavern preset; delete if unused.")
        print("  8. Start writing — the AI reads state.yaml to know where to continue.")

    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", default=".", help="target project directory")
    parser.add_argument("--force", action="store_true", help="overwrite existing files")
    parser.add_argument("--dry-run", action="store_true", help="preview only; do not write")
    args = parser.parse_args()

    ok = init_novel(args.target, force=args.force, dry_run=args.dry_run)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
