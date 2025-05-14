import { useState } from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([
    { from: 'bot', text: 'Hi! I’m AgriBot 🌱. How can I help you today?' }
  ]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { from: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');

    try {
      const res = await fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input }),
        mode: 'cors'
      });

      const data = await res.json();
      const botMessage = { from: 'bot', text: data.reply };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { from: 'bot', text: 'Error fetching response.' }
      ]);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 to-green-100 flex flex-col items-center justify-between p-6">
      <h1 className="text-5xl font-extrabold text-green-700 mb-6 tracking-wide flex items-center gap-2">
        AgriBot <span className="text-3xl">🌾</span>
      </h1>

      <div className="w-full max-w-2xl flex flex-col flex-1 bg-white rounded-2xl shadow-lg p-6 mb-4 overflow-y-auto space-y-4">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`rounded-xl px-4 py-3 max-w-[75%] text-sm sm:text-base leading-relaxed shadow-sm ${
              msg.from === 'bot'
                ? 'bg-green-200 text-left self-start'
                : 'bg-blue-200 text-right self-end ml-auto'
            }`}
          >
            {msg.text}
          </div>
        ))}
      </div>

      <div className="w-full max-w-2xl flex gap-3">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask about crops, soil, fertilizers..."
          className="flex-1 px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-400 text-sm sm:text-base"
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
        />
        <button
          onClick={handleSend}
          className="bg-green-600 hover:bg-green-700 text-white px-6 py-3 rounded-xl font-medium transition"
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default App;
