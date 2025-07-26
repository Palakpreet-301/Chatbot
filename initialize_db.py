import sqlite3

conn = sqlite3.connect('chatbot.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS chatbot_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# Insert sample data
sample_data = [
    ("What is AI?", "AI stands for Artificial Intelligence."),
    ("Who is the Prime Minister of India?", "Narendra Modi is the current Prime Minister of India."),
    ("What is Python?", "Python is a popular programming language.")
]

cursor.executemany("INSERT INTO chatbot_data (question, answer) VALUES (?, ?)", sample_data)

conn.commit()
conn.close()
print("Database initialized with sample data.")
