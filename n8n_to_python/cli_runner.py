# cli_runner.py

import argparse
import json
from utils import node_dispatcher


def transpile_workflow(json_path, output_path="generated_workflow.py"):
    with open(json_path) as f:
        workflow = json.load(f)

    generated_code = []
    for node in workflow.get("nodes", []):
        node_type = node.get("type")
        handler = node_dispatcher.get(node_type)
        if handler:
            generated_code.append(f"# {node['name']}\n" + handler(node))
        else:
            generated_code.append(f"# {node['name']}\n# Unsupported node type: {node_type}")

    with open(output_path, "w") as f:
        f.write("\n\n".join(generated_code))

    print(f"✅ Workflow transpiled to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Transpile an n8n JSON workflow to Python script.")
    parser.add_argument("workflow", help="Path to n8n workflow JSON file")
    parser.add_argument("--output", default="generated_workflow.py", help="Output Python file path")
    args = parser.parse_args()

    transpile_workflow(args.workflow, args.output)


if __name__ == "__main__":
    main()
