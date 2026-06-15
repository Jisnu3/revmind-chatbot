import { useState } from "react";
import API from "../api/api";

function Chat() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
const [loading, setLoading] = useState(false);

const handleSend = async () => {

  setLoading(true);

  try {

    const response = await API.post(
      "/api/chat",
      {
        question
      }
    );

    setAnswer(response.data.answer);

  } catch (error) {

    setAnswer("Something went wrong.");
  }

  setLoading(false);
};

  return (
    <div className="chat-search-card">

    <div className="search-row">

        <input
        type="text"
        placeholder="Ask a business question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        />

        <button
        onClick={handleSend}
        disabled={loading}
        >
        {loading ? "Thinking..." : "Send"}
        </button>

    </div>

    {answer && (
        <div className="recent-answer">

        <h3>Recent Question & Answer</h3>

        <p>
            <span className="question-label">
            Question:
            </span>
            {" "}
            {question}
        </p>

        <div>
        <span className="answer-label">
            Answer:
        </span>
        <pre className="answer-text">
            {answer}
        </pre>
        </div>
        </div>
    )}

    </div>
  );
}

export default Chat;