from flask import Flask, request, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.template_folder = 'templates'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['file-upload']
        # Do something with the uploaded image, for example, save it to disk
        image_file.save("uploaded_image.jpg")
        print("Done")
        return 'Image uploaded successfully!'

    return render_template('index.html')

if __name__ == '__main__':
    app.run()