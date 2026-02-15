#!/usr/bin/env python3
"""Quick note-taking tool with timestamp."""
import sys
from pathlib import Path
from datetime import datetime

NOTES_DIR = Path.home() / ".notes"

def add_note(content, tag=None):
    NOTES_DIR.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fname = NOTES_DIR / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(fname, 'w') as f:
        f.write(f"# {ts}\n")
        if tag: f.write(f"Tag: {tag}\n\n")
        f.write(f"{content}\n")
    print(f"Note saved: {fname.name}")

def list_notes():
    if not NOTES_DIR.exists(): print("No notes yet!"); return
    for n in sorted(NOTES_DIR.glob("*.txt"), reverse=True): print(f"- {n.stem}")

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: quick_note.py <add|list> [args]"); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "add":
        content, tag = " ".join(sys.argv[2:]), None
        if "--tag" in sys.argv:
            i = sys.argv.index("--tag")
            tag, content = sys.argv[i+1], " ".join(sys.argv[2:i])
        add_note(content, tag)
    elif cmd == "list": list_notes()
    else: print(f"Unknown: {cmd}")
