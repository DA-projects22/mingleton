import numpy as np
import faiss
import pickle
import ollama
from sentence_transformers import SentenceTransformer
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="../frontend/build", static_url_path="")
CORS(app)  

# loading MiniLm-L6-v2 model
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Function to retrieve similar romantic texts from faiss.pkl 
def retrieve_romantic_texts(query, top_k=3):
    try:
        with open("faiss_index.pkl", "rb") as f:
            index, love_texts = pickle.load(f)
            query_embedding = np.array(embedder.encode([query])).astype("float32")
            _, indices = index.search(query_embedding, top_k)
            return [love_texts[i] for i in indices[0] if i < len(love_texts)]
    except Exception as e:
        print(f"Error retrieving romantic texts: {e}")
        return ["You are my sunshine", "My heart beats only for you", "Forever in love with you"]

@app.route("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/generate", methods=["POST"])
def generate_love_letter():
    try:
        data = request.get_json()
        print("Received JSON from frontend:", data)  # Debugging log

        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        # Extract and validate required fields
        required_fields = ["receiver", "sender", "tone", "lover_description", "memory"]
        missing_fields = [field for field in required_fields if field not in data or not data[field]]#checking whether all the fields are there

        if missing_fields:#returns error if any field is missing
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Retrieve romantic texts
        r_texts = retrieve_romantic_texts(f"romantic letter for {data['receiver']} in {data['tone']} tone")

        
        prompt = f"""
        You are a world-class poet and writer, skilled in crafting deeply emotional and evocative love letters. 
        Your task is to write the most heartfelt and beautifully written love letter from {data['sender']} to {data['receiver']}. 

        **Details to Incorporate:**
        - **Tone:** Write in a {data['tone']} tone, making sure the emotions are vivid and heartfelt.
        - **Personal Connection:** {data['receiver']} is described by {data['sender']} as: "{data['lover_description']}".
        - **Cherished Memory:** Their most beautiful shared memory is: "{data['memory']}".  
        - **Romantic Inspirations:** Use the following romantic phrases as inspiration: {r_texts}.  

        **Writing Guidelines:**
        1. Begin with a **captivating and intimate opening** that instantly conveys deep affection.
        2. Express **why {data['receiver']} is so special** and how they make {data['sender']} feel.
        3. Include **specific moments** that highlight their love, ensuring it feels deeply personal.
        4. Use **evocative language, poetic metaphors, and sensory details** to make emotions come alive.
        5. End with a **sincere and memorable closing**, reaffirming love and devotion.

        Make the letter as **genuine, expressive, and passionate** as possible—something that will touch {data['receiver']}'s heart and make them feel truly cherished.
        """

        # executing the prompt in llama2 using ollama
        response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])

        print("Ollama Response:", response)  # Debugging log

        # Extract the response text safely
        generated_letter = response.get("message", {}).get("content", "Error generating letter")

        return jsonify({"letter": generated_letter})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
