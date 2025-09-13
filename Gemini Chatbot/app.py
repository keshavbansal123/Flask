from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)
genai.configure(api_key=os.environ.get("your_api_key"))
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp")

chat_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    chat_history.append({"role": "user", "parts": [user_input]})

    try:
        prompt = user_input + "  Please format your response using Markdown."
        response = model.generate_content(chat_history)
        reply = response.text
        chat_history.append({"role": "model", "parts": [reply]})
    except Exception as e:
        reply = f"Error: {e}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)