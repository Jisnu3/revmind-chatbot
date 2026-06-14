import { useState } from "react";
import API from "../api/api";

function Chat() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setAnswer("");

    try {
      const res = await API.post("/api/chat", {
        question,
      });

      setAnswer(res.data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Error communicating with server.");
    }

    setLoading(false);
  };

  return (
    <div className="chat-container">
      <h2>Sales Analytics Chatbot</h2>

      <input
        type="text"
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={askQuestion}>
        Send
      </button>

      {loading && <p>Thinking...</p>}

      {question && (
        <div className="chat-box">
          <h4>Question</h4>
          <p>{question}</p>

          <h4>Answer</h4>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default Chat;