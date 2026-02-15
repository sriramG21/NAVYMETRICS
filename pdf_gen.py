from fpdf import FPDF
import streamlit as st
import bmi as bm
import bodyf as be
import waist as wf
import pulse as pf

def pd(details, results):
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "NavyMetrics Health Report", ln=True, align="C")
    pdf.ln(10)

    # Section: Personal Details
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Personal Details", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.ln(4)

    details = {
        "Name": st.session_state.get("name", "Not entered"),
        "Gender": st.session_state.get("gender", "Not selected"),
        "Height (m)": st.session_state.get("height", "Not entered"),
        "Weight (kg)": st.session_state.get("weight", "Not entered"),
        "Waist (cm)": st.session_state.get("waist", "Not entered"),
        "Hip (cm)": st.session_state.get("hip", "Not entered"),
        "Neck (cm)": st.session_state.get("neck", "Not entered"),
        "Pulse (bpm)": st.session_state.get("pulse", "Not entered")
    }

    # Try calculation
    try:
        bmi_result = bm.bmi(details["Height (m)"], details["Weight (kg)"])
        whr_result = wf.wf(details["Waist (cm)"], details["Hip (cm)"], details["Gender"])
        bfp_result = be.bf(details["Gender"], details["Waist (cm)"], details["Neck (cm)"], details["Hip (cm)"], details["Height (m)"] * 100)
        pulse_result = pf.check_pulse(details["Pulse (bpm)"])
    except Exception as e:
        st.error("Calculation Error: " + str(e))
        bmi_result = whr_result = bfp_result = pulse_result = "Error"

    results = {
        "Body Mass Index (BMI)": bmi_result,
        "Waist-to-Hip Ratio (WHR)": whr_result,
        "Body Fat Percentage": bfp_result,
        "Pulse Status": pulse_result
    }

    for key, value in details.items():
        pdf.cell(0, 8, f"{key}: {value}", ln=True)

    pdf.ln(10)

    # Section: Health Analysis Results
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Health Analysis Results", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.ln(4)

    for key, value in results.items():
        pdf.cell(0, 8, f"{key}: {value}", ln=True)

    return "Navymetrics_report.pdf"  