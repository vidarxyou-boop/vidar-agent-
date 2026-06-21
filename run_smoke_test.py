from pathlib import Path
import sys, json, traceback

sys.path.insert(0, r"F:\AGENT TRAIL")

try:
    from vidar.agent import VidarAgent
except Exception as e:
    print("IMPORT_ERROR", e)
    raise

agent = VidarAgent()
mission = "Dry-run: enumerate actions for adding logging to commands (do not apply)"

try:
    plan = agent._generate_codebase_action_plan(Path('.'), mission)
    print(json.dumps(plan, indent=2))
except Exception as e:
    print("ERROR", e)
    traceback.print_exc()
