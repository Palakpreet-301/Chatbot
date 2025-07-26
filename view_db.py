import sqlite3

def view_database():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chatbot_data")
    rows = cursor.fetchall()

    for row in rows:
        print(f"ID: {row[0]} | Question: {row[1]} | Answer: {row[2]}")

    conn.close()

if __name__ == "__main__":
    view_database()
