import json
from api_nodes import handle_http_request, handle_webhook
from data_nodes import handle_set, handle_if, handle_merge
from db_nodes import handle_mysql, handle_postgresql, handle_mongodb
from control_nodes import handle_cron, handle_delay
from auth_nodes import handle_oauth2
from ai_nodes import handle_openai
from file_nodes import handle_read_file, handle_write_file
from integration_nodes import handle_slack, handle_telegram
from utils import node_dispatcher


def load_n8n_workflow(path):
    with open(path) as f:
        return json.load(f)


def transpile_workflow(n8n_json):
    python_lines = ["# Auto-generated from n8n workflow\n"]
    for node in n8n_json.get("nodes", []):
        handler = node_dispatcher.get(node["type"])
        if handler:
            code = handler(node)
            python_lines.append(code)
        else:
            python_lines.append(f"# Skipping unsupported node: {node['type']}")
    return "\n\n".join(python_lines)


if __name__ == "__main__":
    workflow = load_n8n_workflow("example_workflow.json")
    python_code = transpile_workflow(workflow)
    with open("generated_workflow.py", "w") as f:
        f.write(python_code)
    print("✅ Python workflow generated as generated_workflow.py")
