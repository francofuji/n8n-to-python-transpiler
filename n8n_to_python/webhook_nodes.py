# webhook_nodes.py

def handle_webhook_trigger(node):
    path = node.get("parameters", {}).get("path", "/webhook")
    method = node.get("parameters", {}).get("httpMethod", "POST").upper()
    return (
        "from flask import Flask, request\n"
        "app = Flask(__name__)\n\n"
        f"@app.route('{path}', methods=['{method}'])\n"
        "def webhook():\n"
        "    data = request.get_json()\n"
        "    print('Received webhook:', data)\n"
        "    return {'status': 'ok'}\n\n"
        "if __name__ == '__main__':\n"
        "    app.run(port=5000)"
    )
