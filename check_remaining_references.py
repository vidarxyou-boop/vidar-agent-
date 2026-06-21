import re
from pathlib import Path

root = Path('hermes-agent')
pattern = re.compile(r'hermes|nous', re.I)

matches = []
for path in root.rglob('*'):
    if any(part in {'.git', '.venv', 'node_modules'} for part in path.parts):
        continue
    if path.is_file():
        if path.suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif', '.pdf', '.zip', '.tar', '.gz', '.exe', '.dll', '.so', '.pyc', '.pkl', '.lock'}:
            continue
        try:
            text = path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if pattern.search(line):
                matches.append((str(path), i, line.strip()))
                if len(matches) >= 120:
                    break
    if len(matches) >= 120:
        break

print(len(matches))
for path, line_no, line in matches:
    print(f"{path}:{line_no}: {line}")
