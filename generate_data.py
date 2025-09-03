import pandas as pd
import numpy as np
import random


n = 300  

def generate_health_percentage(row):
    score = 100

    
    if row["age"] > 50:
        score -= 10
    if row["age"] > 65:
        score -= 15

    
    bmi = row["weight"] / ((row["height"]/100) ** 2)
    if bmi < 18.5 or bmi > 30:
        score -= 10

    
    if row["systolic"] > 140 or row["diastolic"] > 90:
        score -= 15
    elif row["systolic"] > 120:
        score -= 5

    
    if row["cholesterol"] == "borderline high":
        score -= 10
    elif row["cholesterol"] == "high":
        score -= 20

    if row["smoking"] == "yes":
        score -= 20

    
    if row["exercise"] == "weekly":
        score -= 5
    elif row["exercise"] == "rare":
        score -= 10
    elif row["exercise"] == "never":
        score -= 20

    
    if row["family_history"] == "yes":
        score -= 15

    return max(10, min(100, score))  


data = []
for _ in range(n):
    age = random.randint(20, 80)
    gender = random.choice(["male", "female"])
    height = random.randint(150, 190)
    weight = random.randint(50, 100)
    systolic = random.randint(100, 170)
    diastolic = random.randint(60, 110)
    cholesterol = random.choice(["normal", "borderline high", "high"])
    smoking = random.choice(["yes", "no"])
    exercise = random.choice(["daily", "weekly", "rare", "never"])
    family_history = random.choice(["yes", "no"])

    row = {
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "systolic": systolic,
        "diastolic": diastolic,
        "cholesterol": cholesterol,
        "smoking": smoking,
        "exercise": exercise,
        "family_history": family_history
    }
    row["heart_health_percentage"] = generate_health_percentage(row)
    data.append(row)


df = pd.DataFrame(data)
df.to_csv("custom_heart.csv", index=False)

# print("custom_heart.csv generated with", n, "rows")
