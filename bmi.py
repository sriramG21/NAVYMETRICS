import streamlit as st
import personal as pp

def bmi(h,w):
    if h==0 or w==0:
        st.error("⚠️ Oops! Looks like something’s missing or incorrect. Please check your input and try again."

)
        
    else:
        bmi=(w/(h*h))
        if bmi < 18.5:
             st.error(f"{bmi}-Underweight 🤕")
        elif bmi < 25:
            st.success(f"{bmi}-Normal weight 😀")
        elif bmi < 30:
            st.warning(f"{bmi}-Overweight 😖")
        elif bmi < 35:
            st.error(f"{bmi}-Obesity (Class 1) 😰")
        elif bmi < 40:
            st.error(f"{bmi}Obesity (Class 2) 💀")
        else:
            st.error(f"{bmi}-Extreme obesity ☠️")
        st.info("""
**Diclaimer:** BMI is a rough estimate and may not accurately reflect your health condition.
It does not distinguish between weight from fat and weight from muscle.
""")
        return f"{bmi:.2f}"

