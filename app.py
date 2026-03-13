from flask import Flask, request, jsonify, render_template
import numpy as np
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load dataset
with open("ai-error-helper/dataset/errors.txt", "r") as f:
    errors = [line.strip() for line in f]

# Load vectors
vectors = np.load("ai-error-helper/vectors.npy")


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Search API
@app.route("/search", methods=["POST"])
def search():

    user_error = request.json["error"]

    query_vector = model.encode([user_error])

    similarities = np.dot(vectors, query_vector.T).flatten()

    best_index = np.argmax(similarities)

    best_line = errors[best_index]

    error, solution = best_line.split("|")

    return jsonify({
        "error": error.strip(),
        "solution": solution.strip()
    })


if __name__ == "__main__":
    app.run(debug=True)