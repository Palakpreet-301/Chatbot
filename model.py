import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM chatbot_data")
    data = cursor.fetchall()
    conn.close()
    return data

def train_model():
    data = load_data()
    questions = [item[0] for item in data]
    
    if not questions:
        return TfidfVectorizer(), None, data  # return empty model

    vectorizer = TfidfVectorizer()
    question_vectors = vectorizer.fit_transform(questions)
    return vectorizer, question_vectors, data

def get_answer(user_input, vectorizer, question_vectors, data, threshold=0.6):
    if question_vectors is None:
        return None, False

    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, question_vectors)
    max_index = similarity.argmax()
    max_score = similarity[0][max_index]

    if max_score > threshold:
        return data[max_index][1], True
    else:
        return None, False
