from flask import render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from server import app
import os
from server import config
from server.tf_idf import get_tf_idf

@app.route('/')
def homepage():
    return render_template('index.html', info=None)


@app.route('/action', methods=['POST'])
def take_action():
    if request.method == 'POST':

        if request.form.get("file_upload"):
            return render_template('file_upload.html')
        elif request.form.get("tf_idf"):
            return render_template('tf_idf.html')
        else:
            return redirect('/')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config[config.ALLOWED_EXTENSIONS]

@app.route('/upload', methods=['POST'])
def upload_files():
    if request.method == 'POST':
        
        if 'file' not in request.files:
            return render_template('index.html', info="Something Went Wrong"), 409

        files = request.files.getlist('file')
        
        atleast_one_file_upload = 0
        atleast_one_file_upload_fail = 0
        message = "Files Uploaded:"
        for each_file in files:
            cache   = app.config[config.CACHE]
            if each_file and allowed_file(each_file.filename):
                filename = secure_filename(each_file.filename)
                file_path= os.path.join(app.config[config.UPLOAD_FOLDER], filename)
                each_file.save(file_path)
                cache.update(file_path)
                message = message+" "+filename
                atleast_one_file_upload = 1
            else:
                atleast_one_file_upload_fail = 1

        
        if atleast_one_file_upload ==1 and atleast_one_file_upload_fail == 1: # Partial success
            return_code = 207
        elif atleast_one_file_upload == 1 and atleast_one_file_upload_fail == 0: # All file(s) are uploaded
            return_code = 200
        elif atleast_one_file_upload == 0 and atleast_one_file_upload_fail == 1: # File upload failed entirely
            return_code = 409
            message     = 'No files are uploaded'

        return render_template('index.html', info=message), return_code



@app.route('/tf-idf', methods=['POST'])
def compute_tfidf_score():
    if request.method == 'POST':

        if request.form.get("back"):
            return render_template("index.html", info=None)
        
        text = request.form['text_field']
        if text == "":
            return render_template('tf_idf.html', info="Please enter text"), 409

        result = get_tf_idf(text)
        if result is None:
            info = "No files present in server. Please upload file"
            return render_template('tf_idf.html', info=info), 409
        
        return render_template('tf_idf.html', results=result), 200