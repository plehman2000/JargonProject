from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from tika import parser

app = Flask(__name__, template_folder='templates')

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

        raw = parser.from_file('static/'+filename)
        content=raw['content'][45:]
        
    return render_template('content.html', content=content) 

if(__name__) == "__main__":
    app.run(Debug=True)

