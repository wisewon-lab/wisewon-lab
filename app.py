import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("student_performance_model.joblib")

st.title("Student Performance Predictor")

# Collect input
gender = st.selectbox("Gender", ["Male", "Female"])
part_time_job = st.selectbox("Part-time Job", ["Yes", "No"])
absence_days = st.number_input("Absence Days", 0, 50, 2)
extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])
study_hours = st.number_input("Weekly Self Study Hours", 0, 40, 10)
career_aspiration = st.text_input("Career Aspiration", "Engineering")

# Subject scores
math = st.slider("Math Score", 0, 100, 70)
history = st.slider("History Score", 0, 100, 60)
physics = st.slider("Physics Score", 0, 100, 72)
chemistry = st.slider("Chemistry Score", 0, 100, 68)
biology = st.slider("Biology Score", 0, 100, 75)
english = st.slider("English Score", 0, 100, 65)
geography = st.slider("Geography Score", 0, 100, 58)

if st.button("Predict Performance"):
    sample = pd.DataFrame([{
        "gender": gender,
        "part_time_job": part_time_job,
        "absence_days": absence_days,
        "extracurricular_activities": extracurricular,
        "weekly_self_study_hours": study_hours,
        "career_aspiration": career_aspiration,
        "math_score": math,
        "history_score": history,
        "physics_score": physics,
        "chemistry_score": chemistry,
        "biology_score": biology,
        "english_score": english,
        "geography_score": geography
    }])
    prediction = model.predict(sample)[0]
    st.success(f"Predicted Performance Category: **{prediction}**")
