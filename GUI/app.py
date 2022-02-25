from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import PyPDF2
from tika import parser

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"

@app.route("/")
def upload_file():
    return render_template('index.html')

@app.route("/display", methods = ['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        
        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file = open(app.config['UPLOAD_FOLDER'] + filename,"rb")
        pdfreader = PyPDF2.PdfFileReader(file)
        x=pdfreader.numPages
        pageobj=pdfreader.getPage(x-1)
        text=pageobj.extractText()
        

        raw = parser.from_file('static/'+filename)
        content=raw['content'][45:]

        #content = file.read()   
        
    return render_template('content.html', content=content) 

if(__name__) == "__main__":
    app.run(Debug=True)

