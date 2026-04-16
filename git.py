#!/usr/bin/env python3
"""
Git utility functions for Claude Code skills
Provides helper functions for common git operations
"""

import subprocess
import os
from typing import List, Optional, Tuple


def run_command(cmd: List[str], cwd: Optional[str] = None) -> Tuple[int, str, str]:
    """
    Execute a git command and return result

    Args:
        cmd: Command as list of strings
        cwd: Working directory (optional)

    Returns:
        Tuple of (return_code, stdout, stderr)
    """
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=cwd
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)


def add_files(pattern: str = ".") -> Tuple[int, str]:
    """
    Add files to git staging area

    Args:
        pattern: File pattern to add (default: all files)

    Returns:
        Tuple of (return_code, message)
    """
    code, stdout, stderr = run_command(["git", "add", pattern])
    if code == 0:
        return code, f"Files added successfully: {stdout}"
    else:
        return code, f"Error adding files: {stderr}"


def commit(message: str) -> Tuple[int, str]:
    """
    Commit staged changes

    Args:
        message: Commit message

    Returns:
        Tuple of (return_code, message)
    """
    code, stdout, stderr = run_command(["git", "commit", "-m", message])
    if code == 0:
        return code, f"Committed successfully: {stdout}"
    else:
        return code, f"Error committing: {stderr}"


def push(remote: str = "origin", branch: str = "main") -> Tuple[int, str]:
    """
    Push commits to remote repository

    Args:
        remote: Remote name (default: origin)
        branch: Branch name (default: main)

    Returns:
        Tuple of (return_code, message)
    """
    code, stdout, stderr = run_command(["git", "push", remote, branch])
    if code == 0:
        return code, f"Pushed successfully to {remote}/{branch}"
    else:
        return code, f"Error pushing: {stderr}"


def status() -> Tuple[int, str]:
    """
    Check git status

    Returns:
        Tuple of (return_code, status_message)
    """
    code, stdout, stderr = run_command(["git", "status"])
    if code == 0:
        return code, stdout
    else:
        return code, stderr


def log(limit: int = 10) -> Tuple[int, str]:
    """
    Show commit history

    Args:
        limit: Number of commits to show

    Returns:
        Tuple of (return_code, log_message)
    """
    code, stdout, stderr = run_command(["git", "log", f"--oneline", f"-n{limit}"])
    if code == 0:
        return code, stdout
    else:
        return code, stderr


def init_repo(path: str) -> Tuple[int, str]:
    """
    Initialize a new git repository

    Args:
        path: Path to initialize

    Returns:
        Tuple of (return_code, message)
    """
    code, stdout, stderr = run_command(["git", "init"], cwd=path)
    if code == 0:
        return code, f"Repository initialized at {path}"
    else:
        return code, f"Error initializing repository: {stderr}"


def create_and_upload_skills():
    """
    Example function demonstrating the complete workflow
    """
    print("Starting git workflow...")

    # Check status
    code, status_msg = status()
    print(f"Status: {status_msg}")

    # Add files
    code, add_msg = add_files(".")
    print(add_msg)

    # Commit if there are changes
    if "Changes to be committed" in status_msg or "new file" in add_msg:
        code, commit_msg = commit("Add git utility functions")
        print(commit_msg)

        # Push to remote
        code, push_msg = push()
        print(push_msg)
    else:
        print("No changes to commit")


if __name__ == "__main__":
    create_and_upload_skills()