import streamlit as st
def contactus():
    c1,c2=st.columns(2)
    with c1:
        st.header("Instagram")
        st.markdown("[📸 Contact us on Instagram](https://www.instagram.com/sriram_zy?igsh=aDdlb2l0Y2hpYW8w)", unsafe_allow_html=True)