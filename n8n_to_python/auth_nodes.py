# auth_nodes.py

def handle_http_basic_auth(node):
    username = node.get("parameters", {}).get("username", "user")
    password = node.get("parameters", {}).get("password", "pass")
    url = node.get("parameters", {}).get("url", "http://example.com")
    return (
        "import requests\n"
        f"response = requests.get('{url}', auth=('{username}', '{password}'))\n"
        "print(response.status_code)\nprint(response.text)"
    )

def handle_oauth2(node):
    token = node.get("parameters", {}).get("accessToken", "your-token")
    url = node.get("parameters", {}).get("url", "http://example.com")
    return (
        "import requests\n"
        f"headers = {{'Authorization': 'Bearer {token}'}}\n"
        f"response = requests.get('{url}', headers=headers)\n"
        "print(response.status_code)\nprint(response.text)"
    )
