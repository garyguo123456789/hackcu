// frontend/src/App.jsx
import { useState } from "react";

export default function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setAnswer("");

    const res = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });
    const data = await res.json();
    setAnswer(data.answer);
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center p-8">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">
        🎓 Class Insight Assistant
      </h1>

      <div className="w-full max-w-2xl bg-white p-6 rounded-2xl shadow-md">
        <textarea
          className="w-full border rounded-xl p-3 mb-4 resize-none"
          rows="4"
          placeholder="Ask something like: Is CS61A hard?"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button
          onClick={handleAsk}
          disabled={loading}
          className="bg-blue-600 text-white px-5 py-2 rounded-xl hover:bg-blue-700 disabled:opacity-50"
        >
          {loading ? "Analyzing..." : "Ask"}
        </button>

        {answer && (
          <div className="mt-6 bg-gray-100 p-4 rounded-xl whitespace-pre-wrap">
            {answer}
          </div>
        )}
      </div>
    </div>
  );
}
