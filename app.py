import os
from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"


@app.route('/')
def home():
    return render_template('index.html')
def chat():
    user_message = request.json.get('message')

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the appropriate model
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    bot_message = response['choices'][0]['message']['content']
    return jsonify({'response': bot_message})

if __name__ == '__main__':
    app.run(debug=True)
