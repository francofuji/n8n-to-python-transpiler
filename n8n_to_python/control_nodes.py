# control_nodes.py

def handle_cron(node):
    cron = node.get("parameters", {}).get("cronExpression", "* * * * *")
    return (
        "# To simulate a cron job in Python, use schedule or APScheduler\n"
        f"print('This task is scheduled with cron: {cron}')"
    )

def handle_delay(node):
    delay = node.get("parameters", {}).get("delay", 1)
    unit = node.get("parameters", {}).get("unit", "seconds")
    multiplier = {"seconds": 1, "minutes": 60, "hours": 3600}.get(unit, 1)
    seconds = delay * multiplier
    return (
        "import time\n"
        f"print('Delaying for {seconds} seconds...')\n"
        f"time.sleep({seconds})"
    )
