from flask import Flask, render_template, request
from PIL import Image
from cgpa import cgpa  
from image_processing import get_mark 
import pandas as pd
import json

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/auto", methods=['GET', 'POST'])
def auto():
    error = None
    data = None
    cgp = None

    if request.method == 'POST':
        if 'picture' in request.files:
            try:
                image = Image.open(request.files['picture'])
                data = get_mark(image)
                data_records = data.to_dict(orient="records")
                print(f"Extracted data: {data_records}")
                
                # Perform CGPA calculation based on extracted data
                data_df = pd.DataFrame(data_records)

                return render_template("automatic.html", data=data_records)
            except PermissionError:
                error = "Permission error while accessing the image."
            except Exception as e:
                error = f"An error occurred while processing the image: {str(e)}"
        if 'sub-code' in request.form:
            try:
                data = []
                for i in range(len(request.form.getlist('sub-code'))):
                    sub_code = request.form.getlist('sub-code')[i]
                    credit = request.form.getlist('credit')[i]
                    gp = request.form.getlist('gp')[i]
                    data.append({'c_code': sub_code, 'credit': credit, 'gp': gp})

                data_df = pd.DataFrame(data)
                cgp = cgpa(data_df)
                return render_template("automatic.html", cgp=cgp, data=data_df.to_dict(orient="records"))
            except Exception as e:
                error = f"An error occurred while processing the data: {str(e)}"

    return render_template("automatic.html", error=error, data=data, cgp=cgp)


@app.route("/manual")
def manual():
    return render_template("manual.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
