from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
import pytesseract
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/upload/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            text = pytesseract.image_to_string(Image.open(file_path))
            return render_template('index.html', text=text)
    return render_template('index.html', text='')

if __name__ == '__main__':
    app.run(debug=True)