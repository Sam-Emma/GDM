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
    w_pregnancy = ""
    sex =""
    q_pregnancy =""
    height = ""
    weight = ""
    miscarriage = ""
    n_pregnancy = ""
    mess = ""
    if request.method == "POST":
        age = request.form["age"]
        sex = request.form["sex"]
        q_pregnancy = request.form["pregnant_q"]
        height = request.form["height"]
        weight = request.form["weight"]
        miscarriage = request.form["miscarriage"]
        n_pregnancy = request.form["n_pregnancy"]
        w_pregnancy = request.form["w_pregnancy"]
        predict_real, FPG, bmi, mess = model.predict(age,sex,q_pregnancy,
                                    height, weight,
                                    miscarriage,
                                    n_pregnancy,w_pregnancy)
    return render_template("index.html",outcome = predict_real, 
                            fpg = FPG, 
                            age_input =age,bmi_input = bmi, 
                            miscarriage_input = miscarriage,
                            n_preg_input = n_pregnancy,
                            w_preg_input = w_pregnancy,
                            height_input = height,
                            weight_input = weight,
                            message = mess
                    )
        

if __name__ == "__main__":
    app.run(debug = True,use_reloader=False)
