import os
import openai
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask import request

app = Flask(__name__)
Bootstrap(app)

openai.api_key = os.getenv("API_KEY")
chat_log = []

def call_chatgpt_api(condition, severity):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'Health condition: {condition}\nSeverity: {severity}\nUser:',
        max_tokens=500,
        temperature=0
    )
    return response.choices[0].text.strip()


def chat(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0,
        max_tokens=500,
    )
    return response.choices[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prompt', methods=['POST'])
def prompt():
    if request.method == 'POST':

        condition = request.form['condition']
        severity = request.form['severity']
        response = call_chatgpt_api(condition, severity)

        return render_template('output.html', response=response,condition=condition,severity=severity)


@app.route('/further', methods=['POST'])
def further():

    input = request.form['input']

    # Append user input to the chat log
    chat_log.append(input)

    # Check if user input is "exit" to stop the chat
    if input.lower() == 'exit':
        return render_template('index.html')

    # Generate the chatbot's response (you can use any NLP engine here)
    chatbot_response = chat(input)

    # Append chatbot response to the chat log
    chat_log.append(chatbot_response)

    return render_template('output.html', chat_log=chat_log)

app.run(debug=True)
