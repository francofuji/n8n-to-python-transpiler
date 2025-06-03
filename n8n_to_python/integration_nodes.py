# integration_nodes.py

def handle_sendgrid_email(node):
    to = node.get("parameters", {}).get("to", "recipient@example.com")
    subject = node.get("parameters", {}).get("subject", "Test Email")
    content = node.get("parameters", {}).get("content", "Hello from SendGrid")
    return (
        "import sendgrid\n"
        "from sendgrid.helpers.mail import Mail\n"
        "sg = sendgrid.SendGridAPIClient(api_key='your-sendgrid-api-key')\n"
        f"message = Mail(from_email='from@example.com', to_emails='{to}', subject='{subject}', plain_text_content='{content}')\n"
        "response = sg.send(message)\n"
        "print(response.status_code)"
    )

def handle_slack_message(node):
    webhook_url = node.get("parameters", {}).get("webhookUrl", "")
    message = node.get("parameters", {}).get("message", "Hello from Slack")
    return (
        "import requests\n"
        f"payload = {{'text': '{message}'}}\n"
        f"response = requests.post('{webhook_url}', json=payload)\n"
        "print(response.status_code)"
    )
