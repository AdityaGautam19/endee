from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load dataset
with open("ai-error-helper/dataset/errors.txt", "r") as f:
    errors = [line.strip() for line in f]

# Convert text into vectors
embeddings = model.encode(errors)

# Save vectors
np.save("ai-error-helper/vectors.npy", embeddings)

print("Embeddings created successfully")