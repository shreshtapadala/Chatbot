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
    user_input = request.form['message'].lower()
    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]

    if any(greeting in user_input for greeting in greetings):
        return jsonify({'message': "How you doin'"})
    
    if user_input == 'how are you' or user_input == 'how r u' or user_input == 'how are you doing' or user_input == 'how are you?' or user_input == 'how r u?':
        return jsonify({'message': "I'm hopeless and awkward and desperate for love!"})
    
    if user_input == 'who are you' or user_input == 'who are you?' or user_input == 'who r u' or user_input == 'who r u?':
        return jsonify({'message': "I am Sara! An AI Chatbot. I make jokes when I am uncomfortable."})
    
    if user_input == 'who is your favorite singer?' or user_input == 'who is your favorite singer':
        return jsonify({'message': "My favorite singer is Pheobe Buffay!"})
    
    if user_input == 'who is your favorite actor?' or user_input == 'who is your favorite actor':
        return jsonify({'message': "My favorite actor is Joey Tribbiani!"})
    
    if user_input == 'who cooks the best?' or user_input == 'who cooks the best':
        return jsonify({'message': "Monica is the best cook!"})
    
    if user_input == 'what is your favorite song?' or user_input == 'what is your favorite song':
        return jsonify({'message': "My favorite song is Smelly cat! by Pheobe Buffay."})
    
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        if "food" in user_input:
            return jsonify({'message': response.choices[0].message.content.strip() + " (Joey doesn't share fooood.)"})
        
        if "music" in user_input or "song" in user_input:
            return jsonify({'message': response.choices[0].message.content.strip() + " (Smelly Cat! Smelly Cat! What are they feeding you?)"})
        
        if "plan" in user_input:
            return jsonify({'message': response.choices[0].message.content.strip() + " (I don't even have a pla!)"})
        
        if "advice" in user_input:
            return jsonify({'message': response.choices[0].message.content.strip() + " (I am not great at advice, can I interest you in a sarcastic comment?)"})
        
        if "motivation" in user_input or "motivate" in user_input:
            return jsonify({'message': response.choices[0].message.content.strip() + " (Don't give up, is that what a dinosaur would do?)"})
        
        if "love" in user_input or "relationship" in user_input:
            return jsonify({'message': response.choices[0].message.content.strip() + " (We were on a break.)"})
        
        if "maths" in user_input or "statistics" in user_input or "calculations" in user_input:
            return jsonify({'message': response.choices[0].message.content.strip() + " (He's a transponster! :) )"})

        if "life" in user_input:
            return jsonify({'message': response.choices[0].message.content.strip() + " (Welcome to the real world! It sucks. You're gonna love it!)"})

        if "clothes" in user_input or "cloth" in user_input or "dress" in user_input or "clothing" in user_input:
            return jsonify({'message': response.choices[0].message.content.strip() + " (Could I be wearing any more clothes?)"})
        
        if "self-defense" in user_input:
            return jsonify({'message': response.choices[0].message.content.strip() + " (Unagi!)"})
        
        if "clean" in user_input or "organize" in user_input:
            return jsonify({'message': response.choices[0].message.content.strip() + " (Not just clean, 'Monica Clean'.)"})
        
        if "know" in user_input:
            return jsonify({'message': response.choices[0].message.content.strip() + " (They don't know that we know they know!)"})
        

        return jsonify({'message': response.choices[0].message.content.strip()})
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
