from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
from cgpa import cgpa
from image_processing import get_mark


app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/auto", methods=['GET','POST'])
def auto():
    if request.method == 'POST':
        image = Image.open(request.form['picture'])
        data = get_mark(image)
        cgpa_core = cgpa(data)
        print(cgpa_core)
    return render_template("automatic.html")


@app.route("/manual")
def manual():
    return render_template("manual.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
