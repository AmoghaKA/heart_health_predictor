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
        # cholestrol = request.form["cholestrol"]
        # smoking = request.form["smoking"]
        # exercise = request.form["exercise"]
        # history = request.form["history"]
        point = 0
        bmi = round(weigth / (heigth*heigth),1)
        if bmi<18.5 and bmi>=30.0:
            point = point +2
        elif (bmi >= 18.5 and bmi<=24.9):
            point = point+15
        elif (bmi >= 25.0 and bmi<=29.9):
            point = point+8
        
        
        if (systolic<120 and diastolic<80):
            point = point +25
        elif ((systolic>=120 and systolic<=139) or (diastolic>=80 and diastolic<=89)):
            point = point + 15
        elif (systolic>=140 or diastolic>=90):
            point = point + 5

        
        return render_template("submit.html",heigth=heigth,weigth=weigth,bmi=bmi,point=point)
    

if __name__ == "__main__":
    app.run(debug=True)
