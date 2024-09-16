from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from model import review_code
from utils.file_parser import extract_code_from_file

app = Flask(__name__)

# Set folder for uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    # Save the uploaded code file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Extract the code from the file
    code = extract_code_from_file(file_path)
    
    # Analyze and review the code
    review = review_code(code)

    return render_template('index.html', review=review, code=code)

if __name__ == '__main__':
    app.run(debug=True)
