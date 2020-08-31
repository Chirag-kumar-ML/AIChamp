import streamlit as st
import pdfplumber
import pandas as pd

st.title("Pdf File Converter")
st.subheader("Welcome in pdf to text converter")


def extract_text(feed):
    lin = []
    lines=""
    with pdfplumber.load(feed) as pdf:
        pages = pdf.pages
        for page in pdf.pages:
            text = page.extract_text()
            for line in text.split('\n'):
                lines+=line
        lin.append(lines)
    #st.text(lin[0])
    return lin 

uploaded_file = st.file_uploader("upload pdf file", type=None, key=None)
if uploaded_file is not None:
    data = extract_text(uploaded_file)
    st.text("Below is the extracted text from PDF file")
    stri=data[0]
    st.text(stri)
     