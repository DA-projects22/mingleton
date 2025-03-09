<img width="1280" alt="readme-banner" src="https://github.com/Sanjeeb-J/Mingleton/blob/main/img/Mingleton.jpg">

# 💌 Love Letter Generator

## Basic Details

### Team Name: Romantic Coders

### Team Members

- **Amandeep S** - Government College of Engineering Kannur - Backend & AI Model Integration
- **Dyuthi K** - Government College of Engineering Kannur - Frontend Development & UI Design

### Project Description

The **Love Letter Generator** is an AI-powered web app that generates personalized love letters based on user inputs. Utilizing **FAISS**, **MiniLM**, and **Llama 2**, the system retrieves romantic phrases and crafts deeply heartfelt messages with a poetic touch.

---

## 🔧 Technical Details

- **Languages Used:** Python, JavaScript
- **Frameworks Used:** Flask, React.js
- **Libraries Used:** FAISS, SentenceTransformers, Ollama, Flask-CORS
- **Tools Used:** FAISS for similarity search, Ollama for AI-generated content

---

## 🚀 Implementation

### 🔹 Backend (Flask)

- Uses **MiniLM-L6-v2** to generate embeddings for romantic text retrieval.
- **FAISS** is used for similarity-based search of romantic phrases.
- **Ollama with Llama 2** generates customized love letters.

### 🔹 Frontend (React.js)

- User-friendly interface for input collection.
- Displays the generated love letter in real-time.
- Features a **Reset** button to clear inputs and start fresh.

---

## 🔧 Installation & Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
python embedding_generator.py
cd ..
```

### Frontend

```bash
cd frontend
npm install
npm start
```

---

## 📷 Screenshots

![Landing Page](image.png)
*The homepage where users can input their details.*

![Generated Love Letter]\(Add screenshot 2 here)
*A beautifully generated love letter based on user input.*

![Error Handling]\(Add screenshot 3 here)
*Example of error handling for missing fields.*

---

## 🎥 Project Demo

[Demo Video Link Here]
*This video demonstrates the full workflow of generating a love letter.*

---

