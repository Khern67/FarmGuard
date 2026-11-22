import sqlite3

database = sqlite3.connect("farmguard.db")
cursor = database.cursor()

tables = cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    AND name NOT LIKE 'sqlite_%'
""").fetchall()

print("\n=== FARMGUARD DATABASE INSPECTION ===")

for (table,) in tables:
    columns = cursor.execute(
        f"PRAGMA table_info({table})"
    ).fetchall()

    count = cursor.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()[0]

    print(f"\nTable: {table}")
    print("Columns:", [column[1] for column in columns])
    print("Records:", count)

database.close()