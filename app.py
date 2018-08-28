import os
from flask import Flask, flash, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename
from PIL import Image

UPLOAD_FOLDER = 'uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 0.5 * 1024 * 1024 # 0.5MB

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'original_photo' not in request.files:
            flash('No file part')
            return redirect(request.url)

        # getting file from parameters
        file = request.files['original_photo']

        # check if the post request has a selected file
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # getting the secure filename
        sec_filename = secure_filename(file.filename)

        # getting the filepaht
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], sec_filename)

        # converting file into a PIL Image
        photo = Image.open(file)
        # getting the watermarker
        watermark = Image.open('static/dog.png')
        # overlaying the watermarker to submitted file
        photo.paste(watermark, (25, 25), watermark)
        # save transformed image
        photo.save(filepath)
        # returning with new image url
        return render_template('home.html', filepath=filepath)
    else:
        # presenting home
        return render_template('home.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run()