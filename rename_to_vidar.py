import os
import re
from pathlib import Path

ROOT = Path("f:/AGENT TRAIL/hermes-agent")
EXCLUDE_DIRS = {".git", ".venv", "node_modules", "__pycache__"}

replacements = [
    (r"hermes-agent", "vidar-agent"),
    (r"Hermes Agent", "Vidar Agent"),
    (r"HERMES_AGENT", "VIDAR_AGENT"),
    (r"hermes_cli", "vidar_cli"),
    (r"HermesCLI", "VidarCLI"),
    (r"hermes_bootstrap", "vidar_bootstrap"),
    (r"HermesBootstrap", "VidarBootstrap"),
    (r"hermes_constants", "vidar_constants"),
    (r"HermesConstants", "VidarConstants"),
    (r"hermes_logging", "vidar_logging"),
    (r"HermesLogging", "VidarLogging"),
    (r"hermes_state", "vidar_state"),
    (r"HermesState", "VidarState"),
    (r"hermes_time", "vidar_time"),
    (r"HermesTime", "VidarTime"),
    (r"hermes_tools", "vidar_tools"),
    (r"hermes_home", "vidar_home"),
    (r"HERMES_HOME", "VIDAR_HOME"),
    (r"Hermes Home", "Vidar Home"),
    (r"hermes", "vidar"),
    (r"Hermes", "Vidar"),
    (r"HERMES", "VIDAR"),
    (r"nous", "vidar"),
    (r"Nous", "Vidar"),
    (r"NOUS", "VIDAR"),
]

# Text replacements in files
changed_files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    rel = Path(dirpath).relative_to(ROOT)
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        continue
    for filename in filenames:
        if filename.endswith((".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".tar.gz", ".pyc", ".pkl", ".exe", ".dll", ".so", ".sqlite", ".png", ".woff", ".woff2")):
            continue
        path = Path(dirpath) / filename
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        new_text = text
        for old, new in replacements:
            new_text = new_text.replace(old, new)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed_files.append(path)

print(f"Updated {len(changed_files)} files with renamed text.")

# Rename files and directories bottom-up
renames = []
for dirpath, dirnames, filenames in os.walk(ROOT, topdown=False):
    rel = Path(dirpath).relative_to(ROOT)
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        continue
    for name in filenames + dirnames:
        if re.search(r"hermes|nous", name, re.I):
            old_path = Path(dirpath) / name
            new_name = name
            for old, new in replacements:
                new_name = new_name.replace(old, new)
            if new_name != name:
                new_path = Path(dirpath) / new_name
                try:
                    old_path.rename(new_path)
                    renames.append((old_path, new_path))
                except Exception as exc:
                    print(f"Failed rename {old_path} -> {new_path}: {exc}")

print(f"Renamed {len(renames)} file/directory paths.")
for old, new in renames[:40]:
    print(f"{old} -> {new}")
