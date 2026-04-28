import os
import pyodbc
import sys

ALLOWED_KEYWORDS = ["SELECT"]  # strict allowlist
DEFAULT_DB_DRIVER = "ODBC Driver 18 for SQL Server"

def is_safe_query(sql):
    sql_upper = sql.strip().upper()
    return any(sql_upper.startswith(k) for k in ALLOWED_KEYWORDS)

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_query.py \"SELECT ...\"")
        return

    sql = sys.argv[1]

    if not is_safe_query(sql):
        print("❌ Only SELECT queries are allowed.")
        return

    conn_str = (
        f"DRIVER={{{os.getenv('DB_DRIVER', DEFAULT_DB_DRIVER)}}};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')}"
    )

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute(sql)

    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()

    print(columns)
    for row in rows[:50]:  # limit output
        print(row)

if __name__ == "__main__":
    main()
  
