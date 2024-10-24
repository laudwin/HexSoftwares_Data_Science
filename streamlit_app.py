import streamlit as st
from PIL import Image
import joblib  # Using joblib for model loading since your model was saved with joblib
import numpy as np

# Load the model
model = joblib.load('model.pkl')

def run():
    #img1 = Image.open('telkom.png')
    #img1 = img1.resize((156, 145))
    #st.image(img1, use_column_width=False)
    st.title("Loan Prediction System")

    # For gender
    gen_display = ('0', '1')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender", gen_options, format_func=lambda x: gen_display[x])

    # For Marital Status
    mar_display = ('0', '1')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    # For education
    edu_display = ('0', '1')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education", edu_options, format_func=lambda x: edu_display[x])

    # For employment status
    emp_display = ('0', '1')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status", emp_options, format_func=lambda x: emp_display[x])

    # For property status
    prop_display = ('0', '1', '2')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area", prop_options, format_func=lambda x: prop_display[x])

    # For credit score
    cred_display = ('0.0', '1.0')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score", cred_options, format_func=lambda x: cred_display[x])

    # Applicant Monthly Income
    mon_income = st.number_input("Applicant's Monthly Income", value=0)

    # Co-Applicant Monthly Income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income", value=0)

    # Loan Amount
    loan_amt = st.number_input("Loan Amount", value=0)

    # Loan duration
    dur_display = ['2 Month', '6 Month', '8 Month', '1 Year', '16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration", dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        elif dur == 1:
            duration = 180
        elif dur == 2:
            duration = 240
        elif dur == 3:
            duration = 360
        elif dur == 4:
            duration = 480
        
        # Prepare the features array
        features = np.array([[gen, mar, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]])
        
        # Print features for debugging (optional)
        st.write('Features:', features)
        
        # Make prediction
        prediction = model.predict(features)
        
        # Interpret the prediction result
        ans = int(prediction[0])
        if ans == 0:
            st.error('According to our Calculations, you will not get the loan')
        else:
            st.success('Congratulations!! you will get the loan')

# Run the app
if __name__ == '__main__':
    run()
