#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
@app.route('/about')
def about_html():
    return render_template('about.html')

@app.route('/contact')
def contact_html():
    return render_template('contact.html')

if __name__ == '__main__':
   app.run(debug=True, port=5000)
