from flask import Flask, render_template, request
from model import train_model, get_answer
from google_search import google_search
from db import insert_data



app = Flask(__name__)

vectorizer, question_vectors, data = train_model()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    global vectorizer, question_vectors, data

    user_input = request.form["question"]
    answer, found = get_answer(user_input, vectorizer, question_vectors, data)

    if not found:
        # Fetch from Google Search
        answer = google_search(user_input)

        # Insert into DB
        if answer:  # Only insert if something was found
            insert_data(user_input, answer)

            # Re-train model to include new data
            vectorizer, question_vectors, data = train_model()

    return render_template("response.html", question=user_input, answer=answer)


if __name__ == "__main__":
    app.run(debug=True)
