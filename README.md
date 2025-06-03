
# n8n Workflow to Python Transpiler

This project converts n8n workflow JSON exports into runnable Python scripts.  
It supports common node types across categories like data manipulation, databases, control flow, authentication, AI integrations, file handling, and webhooks.

## Features

- Transpile nodes such as Set, If, Delay, MySQL, PostgreSQL, MongoDB, OpenAI, Slack, Webhook triggers, and more.
- Modular design: each node category in its own Python module.
- Command-line interface for easy transpilation.
- Extendable architecture for adding new node handlers.

## Installation

```bash
git clone https://github.com/francofuji/n8n-python-transpiler.git
cd n8n-python-transpiler
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
````

## Usage

Transpile a workflow JSON to a Python script:

```bash
python cli_runner.py path/to/workflow.json --output generated_workflow.py
```

Then run the generated script:

```bash
python generated_workflow.py
```

## Project Structure

* `data_nodes.py` - Data processing nodes like Set, If, Merge.
* `db_nodes.py` - Database integrations (MySQL, PostgreSQL, MongoDB).
* `control_nodes.py` - Control flow nodes (Cron, Delay).
* `auth_nodes.py` - Authentication (Basic Auth, OAuth2).
* `ai_nodes.py` - AI integrations (OpenAI, HuggingFace).
* `file_nodes.py` - File read/write nodes.
* `integration_nodes.py` - External services (SendGrid, Slack).
* `webhook_nodes.py` - Webhook trigger handling.
* `utils.py` - Dispatcher mapping node types to handlers.
* `cli_runner.py` - CLI entry point for transpiling workflows.
* `example_workflow.json` - Sample workflow JSON.
* `test_runner.py` - Example test runner.

## Contributing

Contributions welcome! Please open issues or submit pull requests to add more nodes or improve functionality.

