import React, { useState } from "react";
import "./LoveLetterForm.css"; // Import CSS for styling

const LoveLetterForm = () => {
  const [receiver, setReceiver] = useState("");
  const [sender, setSender] = useState("");
  const [tone, setTone] = useState("");
  const [loverDescription, setLoverDescription] = useState(""); 
  const [memory, setMemory] = useState("");
  const [letter, setLetter] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const generateLoveLetter = async () => {
    setError(""); // Reset previous errors
  
    // Check for empty fields
    if (!receiver || !sender || !tone || !loverDescription || !memory) {
      setError("⚠️ Please fill in all fields before generating a love letter.");
      return;
    }
  
    setLoading(true);
    setLetter("");
  
    const requestData = {
      receiver,
      sender,
      tone,
      lover_description: loverDescription, 
      memory,
    };
  
    try {
      const response = await fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestData),
      });
  
      const data = await response.json();
  
      if (!response.ok) {
        throw new Error(data.error || "Failed to generate letter.");
      }
  
      setLetter(data.letter);
    } catch (error) {
      console.error("Error:", error);
      setError(error.message || "Something went wrong.");
    }
  
    setLoading(false);
  };
  const resetForm = () => {
    setReceiver("");
    setSender("");
    setTone("");
    setLoverDescription("");
    setMemory("");
    setLetter("");
    setError("");
  };
  
  return (
    <div className="main-container">
      {/* Form Section */}
      <div className="form-container">
        <h1 className="title">💌 Love Letter Generator</h1>
        
        <label>Receiver's Name</label>
        <input type="text" value={receiver} onChange={(e) => setReceiver(e.target.value)} />
  
        <label>Your Name</label>
        <input type="text" value={sender} onChange={(e) => setSender(e.target.value)} />
  
        <label>Tone</label>
        <input
          type="text"
          placeholder="Enter Tone (e.g., Romantic, Poetic)"
          value={tone}
          onChange={(e) => setTone(e.target.value)}
        />
  
        <label>Describe Your Lover</label>
        <textarea value={loverDescription} onChange={(e) => setLoverDescription(e.target.value)} />
  
        <label>Your Most Beautiful Memory Together</label>
        <textarea value={memory} onChange={(e) => setMemory(e.target.value)} />
  
        <button className="generate-button" onClick={generateLoveLetter} disabled={loading}>
          {loading ? "Generating..." : "Generate Love Letter"}
        </button>
  
        {/* Reset Button */}
        <button className="reset-button" onClick={resetForm}>Reset</button>
  
        {error && <p style={{ color: "black", fontWeight: "bold", marginTop: "10px" }}>⚠️ {error}</p>}
      </div>
  
      {/* Display Generated Letter */}
      {letter && (
        <div className="letter-container">
          <h2>❤️ Your Love Letter</h2>
          <div className="letter-content">
            <p>{letter}</p>
          </div>
        </div>
      )}
    </div>
  );
};  

export default LoveLetterForm;
