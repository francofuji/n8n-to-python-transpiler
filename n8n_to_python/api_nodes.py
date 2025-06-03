# api_nodes.py

def handle_http_request(node):
    url = node.get("parameters", {}).get("url", "http://example.com")
    method = node.get("parameters", {}).get("method", "GET").upper()
    return f"response = requests.{method.lower()}('{url}')\nprint(response.text)"

def handle_webhook(node):
    path = node.get("parameters", {}).get("path", "/webhook")
    return (
        "from flask import Flask, request\n"
        "app = Flask(__name__)\n\n"
        f"@app.route('{path}', methods=['POST'])\n"
        "def webhook():\n"
        "    data = request.json\n"
        "    print('Received webhook:', data)\n"
        "    return 'OK'\n"
        "\n"
        "if __name__ == '__main__':\n"
        "    app.run(port=5000)"
    )
