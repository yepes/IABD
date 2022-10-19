from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
import os
import pytesseract

UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/uploader", methods = ['POST'])
def upload_file():
    NO_VALID_IMAGE = 'No se ha proporcionado una imagen válida'
    if request.method == 'POST' and request.files:
        f = request.files['image']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

        try:
            text = pytesseract.image_to_string(img, 'spa')
        except Exception as e:
            return render_template('results.html', text=NO_VALID_IMAGE)

        return render_template('results.html', text=text)

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
