import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

# Configure the API using the key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from the Gemini model
def get_gemini_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

# Streamlit UI setup
st.title("CVD Prediction AI BOT")
st.markdown("Enhancing Cardiovascular Disease Prediction with LLM: <span style='color:#009933;'>**A Prototype Using Human Vital Signs**</span><br>by <span style='color:#ff6600;'>***Chidozie Louis Uzoegwu***</span>", unsafe_allow_html=True)

# Patient Information Form
st.write ("""
## Normal Vital Signs in Adults
| Vital Sign        | Normal Range            |
|--------------------|-------------------------|
| Body Temperature   | 98.6°F (37°C)           |
| Heart Rate         | 60-100 beats per minute |
| Respiratory Rate   | 12-18 breaths per minute|
| Blood Oxygen       | 95-100%                 |
| Blood Pressure     | 120/80 mm Hg            |
""")
("Patient Information:")
age = st.slider("Age", min_value=1, max_value=100, value=30)
gender = st.radio("Gender", ["Male", "Female"])
heart_rate = st.slider("Heart Rate (beats per minute)", min_value=30, max_value=200, value=75)
respiration_rate = st.slider("Respiration Rate (breaths per minute)", min_value=5, max_value=40, value=15)
body_temperature = st.slider("Body Temperature (°C)", min_value=30.0, max_value=45.0, value=37.0, step=0.1)
blood_pressure_systolic = st.slider("Blood Pressure - Systolic (mm Hg)", min_value=50, max_value=250, value=120)
blood_pressure_diastolic = st.slider("Blood Pressure - Diastolic (mm Hg)", min_value=30, max_value=150, value=80)
oxygen_saturation = st.slider("Blood Oxygen Saturation (%)", min_value=50, max_value=100, value=98)

submit = st.button('Predict CVD')

if submit:
    # Prepare the input prompt using the patient information
    input_prompt = f"""
    Given the patient's information, assess the risk of cardiovascular disease (CVD). Patient details:
    - Age: {age}
    - Gender: {gender}
    - Heart Rate: {heart_rate} bpm
    - Respiration Rate: {respiration_rate} breaths per minute
    - Body Temperature: {body_temperature} °C
    - Blood Pressure - Systolic: {blood_pressure_systolic} mm Hg
    - Blood Pressure - Diastolic: {blood_pressure_diastolic} mm Hg
    - Blood Oxygen Saturation: {oxygen_saturation}%
    
 Provide an analysis in a simple table based on vital signs and physiological characteristics, focusing on measures such as heart rate, respiration rate, body temperature, blood pressure, and oxygen saturation. 
 Consider the normal ranges and their significance in assessing CVD risk. 
 Also, explore the use of machine learning algorithms in predicting vital signs for CVD monitoring and intervention. 
 Include insights on the role of these vital signs in evaluating the basic operations of the human body and their importance in clinical examinations and long-term CVD risk assessment. 
 As part of the conclusion make massive point about enhancing the development and implementation of an innovative Internet of Medical Things (IoMT) -based remote patient monitoring system. 
 Lastly include advice, such as see doctor, eat healthy, exercise, etc, depending on the level of critical assessment.
    """
    response = get_gemini_response(input_prompt)
    st.write(response)
