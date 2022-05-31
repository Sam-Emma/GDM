# -*- coding: utf-8 -*-

from flask import Flask, request,  render_template
import model
app = Flask(__name__)
@app.route("/", methods =["POST","GET"])
def Home():
    predict_real = ""
    FPG = ""
    age = ""
    bmi = ""
    miscarriage = ""
    n_pregnancy = ""
    mess = ""
    if request.method == "POST":
        age = request.form["age"]
        bmi = request.form["bmi"]
        miscarriage = request.form["miscarriage"]
        n_pregnancy = request.form["n_pregnancy"]
        predict_real, FPG, mess = model.predict(age,bmi,miscarriage,n_pregnancy)
    return render_template("index.html",outcome = predict_real, 
                            fpg = FPG, 
                            age_input =age,bmi_input = bmi, 
                            miscarriage_input = miscarriage,
                            n_preg_input = n_pregnancy,
                            message = mess
                    )
        

if __name__ == "__main__":
    app.run(debug = True,use_reloader=False)
