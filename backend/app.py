from flask import Flask, request, jsonify
from ai_chat import kajal_chat
from tts import speak

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message')
    reply = kajal_chat(user_msg)
    audio = speak(reply)
    return jsonify({"reply": reply, "audio": audio})

if __name__ == '__main__':
    app.run()
