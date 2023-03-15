# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect,jsonify
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

def send_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        #model = 'text-davinci-003',
        messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]['message']['content']
    except Exception as e:
        return e
@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=['GET'])
def get_request_json():
    
    question = request.args.get('msg')
    #print("======================================")
    #print("Receive the question:", question)
    res = send_gpt(question)
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0')
