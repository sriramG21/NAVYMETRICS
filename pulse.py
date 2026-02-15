import streamlit as st

def check_pulse(pulse):
    if pulse < 40:
        st.error(f"{pulse}Too Low (Bradycardia - See pulse doctor) 🧟")
    elif pulse <= 60:
        st.success(f"{pulse}-Excellent (Athlete Level) 🏃‍♂️")
    elif pulse <= 75:
        st.success(f"{pulse}Good (Fit) 👍")
    elif pulse <= 90:
        st.warning(f"{pulse}-Average (Acceptable) 🤔")
    elif pulse <= 100:
        st.error(f"{pulse}-Borderline (Needs Improvement) 🥴")
    else:
        st.error( f"{pulse}-Poor (Fails Navy Standard – Possible Tachycardia) ☠️")
    
    return f"Pulse: {pulse}"
