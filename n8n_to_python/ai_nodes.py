# ai_nodes.py

def handle_openai_completion(node):
    prompt = node.get("parameters", {}).get("prompt", "Say something smart")
    model = node.get("parameters", {}).get("model", "gpt-3.5-turbo")
    return (
        "import openai\n"
        "openai.api_key = 'your-openai-api-key'\n"
        f"response = openai.ChatCompletion.create(model='{model}', messages=[{{'role': 'user', 'content': '{prompt}'}}])\n"
        "print(response.choices[0].message['content'])"
    )

def handle_huggingface_transformer(node):
    task = node.get("parameters", {}).get("task", "text-generation")
    model = node.get("parameters", {}).get("model", "gpt2")
    input_text = node.get("parameters", {}).get("input", "Hello world")
    return (
        "from transformers import pipeline\n"
        f"generator = pipeline('{task}', model='{model}')\n"
        f"result = generator('{input_text}')\n"
        "print(result)"
    )
