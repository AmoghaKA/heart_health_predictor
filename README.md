❤️ Heart Health Predictor — Machine Learning Web App

The Heart Health Predictor is a machine-learning–based web application that analyzes medical attributes and predicts the risk of heart disease.
Users can enter health parameters such as age, blood pressure, cholesterol, etc., and the system estimates whether they are at risk or safe.

🚀 Features

✔ Predicts heart disease risk using trained ML model
✔ User-friendly web interface
✔ Real-time prediction based on health inputs
✔ Model + data preprocessing code included
✔ End-to-end pipeline: dataset → model training → deployment

🧠 Tech Stack
Component	Technology
Programming	Python
Machine Learning	Scikit-Learn
Web Framework	Flask
UI	HTML, CSS (Templates)
Others	NumPy, Pandas, Pickle

📁 Project Structure

heart_health_predictor/
│
├── app.py                     # Flask web app
├── train_data.py              # Model training script
├── generate_data.py           # Data generation script (if applicable)
├── heart_health_model.pkl     # Trained model
├── X_columns.pkl              # Encoded feature columns
├── custom_heart.csv           # Dataset
│
├── static/                    # CSS / images
└── templates/                 # HTML pages

🏃 How to Run Locally

1️⃣ Clone the repository
git clone https://github.com/AmoghaKA/heart_health_predictor.git
cd heart_health_predictor

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Flask app
python app.py

4️⃣ Open in browser
http://127.0.0.1:5000/

📊 Model Information

Used ML classification algorithm to predict heart disease 

Trained on numerical + categorical features

Supports model persistence using Pickle (.pkl files)

⚠️ This tool is for educational purposes only.
It should not be treated as medical advice or a substitute for professional diagnosis.

🔮 Future Improvements

Add SHAP explainability plots (show why user is predicted at risk)

Add more medical/lifestyle features

Deploy on cloud (Render / Railway / Azure / AWS / GCP)

👨‍💻 Author :
Amogha K A
Feel free to ⭐ the repository if you like this project!
