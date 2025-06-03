# db_nodes.py

def handle_mysql(node):
    query = node.get("parameters", {}).get("query", "SELECT 1")
    return (
        "import mysql.connector\n"
        "conn = mysql.connector.connect(user='root', password='pass', host='localhost', database='test')\n"
        "cursor = conn.cursor()\n"
        f"cursor.execute(\"{query}\")\n"
        "for row in cursor.fetchall():\n    print(row)\n"
        "cursor.close()\nconn.close()"
    )

def handle_postgresql(node):
    query = node.get("parameters", {}).get("query", "SELECT 1")
    return (
        "import psycopg2\n"
        "conn = psycopg2.connect(dbname='test', user='postgres', password='pass', host='localhost')\n"
        "cursor = conn.cursor()\n"
        f"cursor.execute(\"{query}\")\n"
        "for row in cursor.fetchall():\n    print(row)\n"
        "cursor.close()\nconn.close()"
    )

def handle_mongodb(node):
    collection = node.get("parameters", {}).get("collection", "test")
    query = node.get("parameters", {}).get("query", {})
    return (
        "from pymongo import MongoClient\n"
        "client = MongoClient('mongodb://localhost:27017/')\n"
        "db = client.get_database('test')\n"
        f"results = db['{collection}'].find({query})\n"
        "for doc in results:\n    print(doc)"
    )
