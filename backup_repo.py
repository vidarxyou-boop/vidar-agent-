import shutil
from pathlib import Path
from datetime import datetime

root = Path('.').resolve()
stamp = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
backup_dir = root / f'.vidar_backup_{stamp}'
ignore_names = {'.venv', '__pycache__', '.git', '.vs', '.vscode', 'venv'}

def ignore_func(path, names):
    return [n for n in names if n in ignore_names]

shutil.copytree(root, backup_dir, ignore=shutil.ignore_patterns('.venv', '__pycache__', '.git', '.vs', '.vscode', 'venv'))
print(f'Backup created at: {backup_dir}')
