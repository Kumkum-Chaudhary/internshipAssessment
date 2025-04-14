import streamlit as st
import pdfplumber
from datetime import datetime

st.set_page_config(page_title="📄 Earnings Call Summarizer", layout="wide")

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def summarize_text(text, max_sentences=10):
    sentences = text.split(". ")
    return ". ".join(sentences[:max_sentences])

st.markdown(
    """
    <h1 style='text-align: center; color: #004488;'>📊 PDF Earnings Call Summarizer</h1>
    <p style='text-align: center; font-size: 18px;'>Upload an earnings call PDF to extract key insights instantly.</p>
    """, unsafe_allow_html=True
)

uploaded_file = st.file_uploader("📁 Upload a PDF file", type=["pdf"], label_visibility="collapsed")

if uploaded_file:
    with st.spinner("🔍 Extracting text from PDF..."):
        extracted_text = extract_text_from_pdf(uploaded_file)

    if extracted_text:
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("📄 Extracted Full Text")
            st.text_area("Extracted Text", extracted_text, height=400)

        with col2:
            st.subheader("🧠 Summary")
            summary = summarize_text(extracted_text)
            st.text_area("Key Highlights", summary, height=400)

        st.success("✅ Summary generated successfully!")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        st.caption(f"📅 Generated on: {timestamp}")
    else:
        st.error("❌ No text could be extracted from the PDF.")
else:
    st.info("📌 Upload a PDF file to get started.")
