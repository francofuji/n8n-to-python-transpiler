# data_nodes.py

def handle_set(node):
    values = node.get("parameters", {}).get("values", {})
    assignments = [f"{k} = {repr(v)}" for k, v in values.items()]
    return "\n".join(assignments)

def handle_if(node):
    condition = node.get("parameters", {}).get("condition", {})
    lhs = condition.get("value1", "a")
    op = condition.get("operation", "equal")
    rhs = condition.get("value2", "b")
    py_op = {
        "equal": "==",
        "notEqual": "!=",
        "larger": ">",
        "smaller": "<"
    }.get(op, "==")
    return f"if {lhs} {py_op} {rhs}:print('Condition met')\nelse:\n    print('Condition not met')"

def handle_merge(node):
    mode = node.get("parameters", {}).get("mode", "mergeByIndex")
    return (
        "# Simulated merge operation\n"
        f"print('Merging inputs with mode: {mode}')"
    )
