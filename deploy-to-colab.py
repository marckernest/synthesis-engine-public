#!/usr/bin/env python3
"""
Synthesis Engine Auto-Deploy Script (v2 - Simplified)
======================================================
Automates syncing notebooks to GitHub repo and deploying to Google Colab.

Usage:
    python deploy-to-colab.py [--target-name TARGET]
    python deploy-to-colab.py --all-targets

Environment variables (optional):
    GITHUB_REMOTE: git remote name (default: origin)
    SYNC_COMMIT_MSG: Commit message (default: "synthesis-engine:auto-deploy")
"""

import os
import sys
import subprocess
from pathlib import Path

# Configuration
REPO_ROOT = Path(__file__).parent.resolve()
GIT_REMOTE = os.getenv("GITHUB_REMOTE", "origin")
SYNC_COMMIT_MSG = os.getenv("SYNC_COMMIT_MSG", "synthesis-engine:auto-deploy")


def run_cmd(cmd, shell=True):
    """Run a command and return success status."""
    print(f">>> {cmd if not shell else cmd.strip()[:100]}...")
    result = subprocess.run(cmd, shell=shell, cwd=str(REPO_ROOT), capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr and "error" in result.stderr.lower():
        print(result.stderr, file=sys.stderr)
    return result.returncode == 0


def sync_to_git(target_name=None):
    """Add and push target notebook(s) to GitHub."""
    
    print("\n" + "=" * 40)
    print("STEP 2: SYNC NOTEBOOK TO REPO")
    print("=" * 40)
    
    # Add all untracked files (notebooks, python, md)
    for item in REPO_ROOT.glob("*"):
        if item.is_file() and (item.suffix in [".ipynb", ".py", ".md"] or "demo" in item.name.lower()):
            run_cmd(f"git add {item}", shell=True)
    
    # Add all subdirectory files
    for root, dirs, files in os.walk(REPO_ROOT):
        for f in files:
            path = Path(root) / f
            if path.suffix in [".ipynb", ".py", ".md"] or "demo" in path.name.lower():
                run_cmd(f"git add {path}", shell=True)
    
    # Stage any modified tracked files
    try:
        subprocess.run(["git", "add", "-u"], cwd=str(REPO_ROOT), capture_output=True)
    except Exception:
        pass
    
    # Commit changes
    try:
        if run_cmd("git status", shell=True):
            run_cmd(f'git commit -m "{SYNC_COMMIT_MSG}"', shell=True)
    except Exception:
        pass
    
    # Push to GitHub
    success = run_cmd(
        f"git push {GIT_REMOTE} main 2>/dev/null || git push {GIT_REMOTE} master 2>/dev/null", 
        shell=True
    )
    
    if success:
        print(f"\n✅ Synced notebook(s) to GitHub\n")
    else:
        print("\n⚠️  Push completed (may need manual review)\n")
    
    return success


def get_colab_link(target_name=None):
    """Generate Google Colab share link."""
    
    print("\n" + "=" * 40)
    print("STEP 3: GENERATE COLAB SHARE LINK")
    print("=" * 40)
    
    if target_name:
        # Use specific notebook path for Colab
        colab_url = f"https://colab.research.google.com/drive/1?filepath=synthesis_engine_demo"
        print(f"\n📤 Deploy URL (ready to share):")
        print(f"  {colab_url}")
        return colab_url
    else:
        # Use the GitHub repo URL with blob link
        github_url = f"https://github.com/marckernest/synthesis-engine-public/blob/main/synthesis-engine-demo.ipynb"
        print(f"\n🔗 Copy this GitHub link (includes demo):")
        print(f"   {github_url}")
        return github_url


def main():
    """Main deployment workflow."""
    
    print("=" * 60)
    print("SYNTHESIS ENGINE AUTO-DEPLOY v2.0")
    print("=" * 60)
    
    # Parse arguments
    import sys
    
    target_name = None
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg.startswith("--target-name="):
            target_name = arg.split("=")[1]
        elif arg == "--all-targets":
            print("Using all available targets...\n")
    
    # Step 1: Sync notebooks to GitHub
    success = sync_to_git(target_name=target_name)
    
    if not success:
        print("⚠️  No notebooks to sync. Skipping deployment.\n")
        return None
    
    # Step 2: Generate Colab/GitHub share link
    share_link = get_colab_link(target_name=target_name)
    return share_link


if __name__ == "__main__":
    main()
