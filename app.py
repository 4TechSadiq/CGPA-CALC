from flask import Flask, render_template, request
from PIL import Image
from cgpa import cgpa  
from image_processing import get_mark 
import pandas as pd
import json
from contact import send_mail

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
                
                print(data)
                data_df = pd.DataFrame(data)
                cgp = cgpa(data_df)
                return render_template("automatic.html", cgp=cgp, data=data_df.to_dict(orient="records"))
            except Exception as e:
                error = f"An error occurred while processing the data: {str(e)}"

    return render_template("automatic.html", error=error, data=data, cgp=cgp)


@app.route("/manual", methods=['GET', 'POST'])
def manual():
    data = []
    cgp = None
    error = None

    if request.method == "POST":
        if 'add_entry' in request.form:
            sub = request.form["sub"]
            credit = request.form["cred"]
            mark = request.form["mark"]
            new_entry = {"s": sub, "c": credit, "m": mark}

            for entry in request.form.getlist('data'):
                s, c, m = entry.split('|')
                data.append({"s": s, "c": c, "m": m})

            data.append(new_entry)

        if 'calculate' in request.form:
            for i in range(len(request.form.getlist('sub'))):
                s = request.form.getlist('sub')[i]
                c = request.form.getlist('credit')[i]
                m = request.form.getlist('marks')[i]
                data.append({"s": s, "c": c, "m": m})

            try:
                data_df = pd.DataFrame(data)
                cgp = cgpa(data_df)
            except Exception as e:
                error = f"An error occurred while processing the data: {str(e)}"

    return render_template("manual.html", data=data, cgp=cgp, error=error)



@app.route("/contact", methods=['GET', 'POST'])
def contact():

    if request.method == "POST":
        name  = request.form["user"]
        mail = request.form["mail"]
        message = request.form["message"]

        if send_mail(name=name,mail=mail,msg=message):
            return render_template("contact.html", msg="Thanks for giving us your valuable feedback.")



    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
