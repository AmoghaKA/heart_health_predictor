from flask import Flask, render_template,request
import joblib
import pandas as pd
# import numpy as np

model = joblib.load(open("heart_health_model.pkl", "rb"))
X_columns = joblib.load("X_columns.pkl")  


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["GET","POST"])  
def submit():
    if request.method == "POST":
        height = float(request.form["height"])
        weight = int(request.form["weight"])
        age = int(request.form["age"])
        gender = request.form["gender"]
        systolic = int(request.form["systolic"])
        diastolic = int(request.form["diastolic"])
        cholesterol = request.form.get("cholesterol")
        smoking = request.form.get("smoking")
        exercise = request.form.get("exercise")
        history = request.form["history"]

        sample = pd.DataFrame([{
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "systolic": systolic,
        "diastolic": diastolic,
        "cholesterol": cholesterol,
        "smoking": smoking,
        "exercise": exercise,
        "family_history": history
    }])

    
    sample_encoded = pd.get_dummies(sample)
    sample_encoded = sample_encoded.reindex(columns=X_columns, fill_value=0)

    
    prediction = model.predict(sample_encoded)[0]
    prediction = round(prediction, 2)


    return render_template("submit.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
