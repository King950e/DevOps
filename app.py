# DevOps course Flask Application
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:0.5b"

@app.route("/")
def main():
    return ">Hello, and Welcome to My Home Lab Project!"

@app.route("/services")
def services():
    return "Version 1 work in progress!"

@app.route("/chat")
def chat_page():
    return CHAT_HTML

@app.route("/api/chat", methods=["POST"])
def chat_api():
    user_message = request.json.get("message", "")
    r = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": user_message,
        "stream": False
    })
    return jsonify({"reply": r.json().get("response", "")})

CHAT_HTML = """
<!doctype html>
<html>
<head><title>Homelab Chat</title>
<style>
  body { font-family: sans-serif; max-width: 600px; margin: 40px auto; }
  #log { border: 1px solid #ccc; padding: 10px; height: 300px; overflow-y: auto; margin-bottom: 10px; }
  .user { color: #2a78d6; font-weight: bold; }
  .bot { color: #333; }
  input { width: 78%; padding: 8px; }
  button { padding: 8px 12px; }
</style>
</head>
<body>
  <h2>Homelab Chat</h2>
  <div id="log"></div>
  <input id="msg" type="text" placeholder="Ask something...">
  <button onclick="send()">Send</button>
  <script>
    async function send() {
      const input = document.getElementById('msg');
      const log = document.getElementById('log');
      const text = input.value;
      if (!text) return;
      log.innerHTML += '<p class="user">You: ' + text + '</p>';
      input.value = '';
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: text})
      });
      const data = await res.json();
      log.innerHTML += '<p class="bot">Bot: ' + data.reply + '</p>';
      log.scrollTop = log.scrollHeight;
    }
    document.getElementById('msg').addEventListener('keydown', e => {
      if (e.key === 'Enter') send();
    });
  </script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
    app.run(debug=True, host="0.0.0.0", port=8080)
