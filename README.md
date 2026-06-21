# Vidar Agent

A terminal-based agent scaffold for the `vidar` command.

## Overview

This project provides a starting point for an advanced Vidar-style agent that can be launched from the command line, plan tasks, execute actions, and persist its state.

## Install

1. Open a terminal in this workspace.
2. Create a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies and the package in editable mode:

```powershell
python -m pip install --upgrade pip
python -m pip install -e .
```

## Usage

- Launch the agent:
  ```powershell
vidar wake --mission "Build a terminal-based Vidar agent from scratch"
```
- Run a shell command:
  ```powershell
vidar shell --cmd "dir"
```
- Talk to a local Ollama model:
  ```powershell
vidar talk --prompt "Explain the Vidar agent architecture"
```
- Configure the model provider or model name:
  ```powershell
vidar config --provider ollama --model llama2
```
- Generate a mission plan:
  ```powershell
vidar plan --mission "Create a Vidar plugin system"
```
- Initialize a workspace:
  ```powershell
vidar init --path .\my-workspace
```
- Execute commands in a shell engine:
  ```powershell
vidar exec --engine powershell --cmd "Get-ChildItem"
```
- Perform filesystem operations:
  ```powershell
vidar fs create --path .\newfile.txt --content "Hello"
vidar fs write --path .\existing.py --content "print('updated')"
vidar fs read --path .\existing.py
vidar fs delete --path .\old-folder --force
vidar fs list --path .\src
```
- Ask Vidar to perform a natural-language action:
  ```powershell
vidar act --instruction "Create a README.md and a src/app.py file with a starter function"
```
- Analyze the current codebase and suggest a refactor or feature plan:
  ```powershell
vidar analyze --path . --mission "Add a new CLI command to Vidar"
```
- Apply generated code changes automatically:
  ```powershell
vidar apply --path . --mission "Add unit tests and improve CLI help"
```
  or with an explicit instruction:
  ```powershell
vidar apply --path . --instruction "Create vidar/tests/test_cli.py and add tests for the run_shell command"
```
- Run Vidar autonomously to plan and apply changes for a mission:
  ```powershell
vidar run --path . --mission "Add logging to all commands"
```
- Install a GitHub package or local repository:
  ```powershell
vidar install --repo https://github.com/<user>/<repo>.git
```
  or
  ```powershell
vidar install --path . --editable
```
- Show saved status:
  ```powershell
vidar status
```

## Notes

- This scaffold includes a plugin-friendly architecture and a state persistence layer.
- Vidar loads supported model provider plugins from `vidar/plugins`.
- On Windows, the `vidar.cmd` script can launch the agent from the repository root.

- This scaffold includes a plugin-friendly architecture and a state persistence layer.
- On Windows, the `vidar.cmd` script can launch the agent from the repository root.
