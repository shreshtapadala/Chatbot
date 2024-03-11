from flask import Flask, render_template, request, jsonify
import openai
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key = "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")

initial_message = "Hi, I'm Sara!"

@app.route('/')
def index():
    return render_template('index.html', initial_message=initial_message)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        return jsonify({'message': response.choices[0].message.content.strip()})
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)