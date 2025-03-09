import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
import pickle

#‼️‼️RUN ONLY ONCE ‼️‼️

#loads MiniLM model from sentence-transformers which convert text into dense vector embedding for similaroty search
embedder=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")




#list of romantic phrases
love_texts = [
    "My love for you is as infinite as the stars in the sky.",
    "Every moment with you feels like a beautiful dream.",
    "You are my sunshine on the darkest days.",
    "Your smile is my favorite melody.",
    "Loving you is the best decision I've ever made.",
    "Holding your hand makes my world complete.",
    "Your eyes shine brighter than the moonlit sky.",
    "Your laughter is the sweetest symphony I’ve ever heard.",
    "No matter where I am, as long as I’m with you, I’m home.",
    "Your love is the light that guides me through the darkest times.",
    "Every heartbeat of mine whispers your name.",
    "The warmth of your embrace feels like the safest place on earth.",
    "With you, every second is a cherished memory in the making.",
    "Your voice is my favorite melody, and your love is my favorite story.",
    "I fall in love with you more and more every single day.",
    "No poem, no song, no painting could ever capture the beauty of our love.",
    "You are the dream I never want to wake up from.",
    "The love we share is a masterpiece, painted with the colors of our souls.",
    "In your eyes, I find my paradise.",
    "Loving you is like breathing—I simply can't stop.",
    "Every time I see you, my heart races like it did the first time we met.",
    "No matter how much time passes, I will always choose you, again and again.",
]

def create_faiss_index():

    #Creates and saves a FAISS index for romantic texts
    embeddings=np.array(embedder.encode(love_texts)).astype("float32")

    index=faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    with open("faiss_index.pkl","wb") as f:
        pickle.dump((index,love_texts),f)

    print("romantic texts saved locally in FAISS")



if __name__=="__main__":
    create_faiss_index()