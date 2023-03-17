# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect,jsonify
import openai
import os
from dotenv import load_dotenv
from revChatGPT.V3 import Chatbot
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
chatbot = Chatbot(api_key=openai.api_key)
def send_gpt(prompt):
    try:
        # 单论对话api
        '''
        response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        #model = 'text-davinci-003',
        messages=[{"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."},
        {"role": "user", "content": prompt}]
        )
        return response["choices"][0]['message']['content']
        '''
        # 多轮对话api
        response = chatbot.ask(prompt)
        return str(response)
    except Exception as e:
        return e
@app.route("/")
def home():
    chatbot.reset()
    #chatbot.ask("hello")
    return render_template("chat.html")
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/logout')
def logout():
    # 执行用户登出操作
    return "Logout successful!"

@app.route("/get", methods=['GET'])
def get_request_json():
    
    question = request.args.get('msg')
    #print("======================================")
    #print("Receive the question:", question)
    res = send_gpt(question)
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0')
