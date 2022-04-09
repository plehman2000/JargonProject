from flask import Flask, request, render_template, json, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
import pdfplumber

app = Flask(__name__)

app.config["FLASK_APP"] = "app.py"

Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'


#initial page to upload pdf
@app.route("/")
def home():
    return "all good"

#displays the uploaded pdf
@app.route('/gettext', methods = ['POST', 'GET'])
def display_file():
    if(request.method == 'POST'):
        pdf = pdfplumber.open(request.files['file'])
        page=0
        content=""
        while page < len(pdf.pages):
                content+="\n" + pdf.pages[page].extract_text()
                page+=1
        pdf.close()
        print(content)
        return content 
    
if(__name__) == "__main__":
    app.run()

