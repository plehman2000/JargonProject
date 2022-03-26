from time import process_time
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import pdfplumber

app = Flask(__name__, template_folder='templates')

app.config["UPLOAD_FOLDER"] = "static/"
app.config["FLASK_APP"] = "app.py"

#initial page to upload pdf
@app.route("/")
def upload_file():
    return render_template('index.html')

#displays the uploaded pdf
@app.route("/display", methods = ['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(app.config['UPLOAD_FOLDER'] + filename)

        pdf = pdfplumber.open('static/'+filename)
        page=0
        content=""
        while page < len(pdf.pages):
            content+="\n" + pdf.pages[page].extract_text()
            page+=1
        pdf.close()
    return render_template('content.html', content=content) 

#clears out current static folder
@app.route("/delete")
def delete_files():
    dir = "static/"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    return render_template('index.html')
    
if(__name__) == "__main__":
    app.run()

