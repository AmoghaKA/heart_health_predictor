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
        try:
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
        
            if prediction <20:
                suggestion = [
                "Maintain a balanced diet with fruits and vegetables.",
                "Exercise regularly but within safe limits.",
                "Avoid smoking and excessive alcohol consumption.",
                "Manage stress through meditation or yoga.",
                "Get regular health check-ups.",
                "Stay hydrated throughout the day.",
                "Maintain a healthy weight.",
                "Limit salt and sugar intake.",
                "Get adequate sleep every night."]

            elif 20<=prediction<50:
                suggestion = [
                "Seek medical advice immediately.",
                "Avoid sudden physical movements.",
                "Check for symptoms like dizziness or chest pain.",
                "Eat healthy food.",
                ]

            elif 50<=prediction<=80:
                suggestion = [
                "Maintain a consistent exercise routine like walking or cycling.",
                "Focus on reducing stress with meditation or breathing exercises.",
                "Include more whole grains, fruits, and vegetables in your meals.",
                "Limit processed foods and sugary drinks.",
                "Schedule regular health check-ups to track progress."] 

            elif prediction>=80:
                suggestion = [
                "Keep up your regular exercise to maintain heart strength.",
                "Continue eating a balanced diet rich in nutrients.",
                "Stay hydrated and get quality sleep every night.",
                "Avoid unhealthy habits like smoking or excessive alcohol.",
                "Go for periodic health check-ups to stay on track."]


            return render_template("submit.html", prediction=prediction,suggestion=suggestion)
        
        except ValueError:
            return render_template("index.html", error="Invalid input. Please enter valid numbers.")
            



@app.route("/back")
def back():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
