from flask import render_template, request
from app import app

app.config["UPLOAD_FOLDER"] = "static/"

@app.route("/")
def upload_file():
    return render_template('index.html')

@app.route("/display", methods = ['Get', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        content = file.read()   
        
    return render_template('content.html', content=content) 