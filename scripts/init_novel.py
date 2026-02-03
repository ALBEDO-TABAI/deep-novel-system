
import os
import shutil
import sys
from pathlib import Path

def init_novel(target_path):
    """
    Initialize a new novel project at the target path.
    Copies the template from the skill's assets directory.
    """
    target_dir = Path(target_path).resolve()
    
    # Determine the skill's assets directory
    # This script is in <skill>/scripts/, so assets is in <skill>/assets/
    script_dir = Path(__file__).parent
    skill_dir = script_dir.parent
    template_dir = skill_dir / "assets" / "template"
    
    if not template_dir.exists():
        print(f"❌ Error: Template directory not found at {template_dir}")
        return False
        
    print(f"🚀 Initializing new novel project at: {target_dir}")
    
    try:
        # Copy the template directory to the target directory
        # shutil.copytree requires the destination to NOT exist, or use dirs_exist_ok=True (Python 3.8+)
        shutil.copytree(template_dir, target_dir, dirs_exist_ok=True)
        print("✅ Template files copied successfully.")
        
        # Optional: Initialize a task.md if not present in template (assuming template has basic structure)
        # For now, we trust the template structure.
        
        print("\nProject initialization complete!")
        print("Recommended next steps:")
        print(f"1. Open the directory: {target_dir}")
        print("2. Review `config/instruction.md` to adjust settings.")
        print("3. Start with `plans/outline.md` (if available) or create your own.")
        
        return True
        
    except Exception as e:
        print(f"❌ Error initializing project: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        target = "."
    else:
        target = sys.argv[1]
        
    init_novel(target)
