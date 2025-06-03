# file_nodes.py

def handle_read_file(node):
    file_path = node.get("parameters", {}).get("path", "./file.txt")
    return (
        f"with open('{file_path}', 'r') as f:\n    content = f.read()\n    print(content)"
    )

def handle_write_file(node):
    file_path = node.get("parameters", {}).get("path", "./output.txt")
    content = node.get("parameters", {}).get("content", "Hello, world!")
    return (
        f"with open('{file_path}', 'w') as f:\n    f.write({repr(content)})\n    print('File written:', '{file_path}')"
    )
