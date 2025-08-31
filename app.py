from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["GET","POST"])  
def submit():
    if request.method == "POST":
        heigth = float(request.form["heigth"])
        weigth = int(request.form["weigth"])
        # age = int(request.form["age"])
        # gender = request.form["gender"]
        systolic = int(request.form["systolic"])
        diastolic = int(request.form["diastolic"])
        cholestrol = request.form.get("cholestrol")
        smoking = request.form.get("smoking")
        exercise = request.form.get("exercise")
        history = request.form["history"]
        point = 0
        bmi = round(weigth / (heigth*heigth),1)
        if bmi<18.5:
            point = point +2
        elif (18.5 <= bmi <= 24.9):
            point = point+15
        elif (25.0 <= bmi <= 29.9):
            point = point+8
        elif bmi>=30:
            point = point +2
        
        if (systolic<120 and diastolic<80):
            point = point +25
        elif ((120<=systolic<=139) or (80<=diastolic<=89)):
            point = point + 15
        elif (systolic>=140 or diastolic>=90):
            point = point + 5

        if(cholestrol == "Normal"):
            point = point + 15
        elif(cholestrol == "Borderline High"):
            point = point + 10
        elif(cholestrol == "High"):
            point = point + 5

        
        if(smoking == "Yes"):
            point = point + 0
        elif(smoking == "No"):
            point = point + 15

        if(exercise == "Daily"):
            point = point + 15
        elif(exercise == "Weekly"):
            point = point + 10
        elif(exercise == "Rare" or exercise == "Never"):
            point = point + 3
        
        if(history == "Yes"):
            point = point + 0
        elif(history == "No"):
            point = point + 15
        max_score = 100
        percentage = round((point/max_score)*100,1)
        return render_template("submit.html",heigth=heigth,weigth=weigth,bmi=bmi,point=percentage)
    

if __name__ == "__main__":
    app.run(debug=True)
