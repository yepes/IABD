from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
import os
import pytesseract
import requests

UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def download_image(url, file_name):
    headers = {
        "User-Agent": "Chrome/51.0.2704.103",
    }
    response = requests.get(url, headers=headers)

    # Save the image
    if response.status_code == 200:
        print('Response OK')
        with open(file_name, "wb") as f:
            f.write(response.content)
            print()
    else:
        print('Response not OK')
        print(response.status_code)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/uploader", methods=['POST'])
def upload_file():
    NO_VALID_IMAGE = 'No se ha proporcionado una imagen válida'

    if request.method == 'POST':

        print('es post')
        url = request.form.get("url")
        filename = request.form.get("filename")
        filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))

        download_image(url, filename)

        # f = request.files['image']
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        # img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        img = Image.open(filename)
        try:
            text = pytesseract.image_to_string(img, 'spa')
        except Exception as e:
            return render_template('results.html', text=NO_VALID_IMAGE)

        # myobj = gTTS(text=text, lang="es", slow=False)
        # myobj.save(app.config['UPLOAD_FOLDER'] + '/speech.mp3')
        # playsound(app.config['UPLOAD_FOLDER'] + '/speech.mp3')

        return render_template('results.html', text=text)

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
