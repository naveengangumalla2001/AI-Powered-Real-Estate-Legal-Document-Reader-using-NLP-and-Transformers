import streamlit as st
import tempfile

from pdf_reader import read_pdf
from ner import extract_entities
from entity_formatter import organize_entities
from summarizer import summarize_text
from question_answer import answer_question
from risk_detector import detect_risksn

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AI Real Estate Legal Document Reader",
    page_icon="🏠",
    layout="wide"
)

# ==========================================
# Sidebar
# ==========================================

st.sidebar.title("🏠 AI Document Reader")

st.sidebar.markdown("""
### Features

✅ PDF Upload

✅ Text Extraction

✅ Named Entity Recognition (NER)

✅ Document Summary

✅ Risk Detection

✅ Question Answering
""")

# ==========================================
# Main Title
# ==========================================

st.title("🏠 AI-Powered Real Estate Legal Document Reader")

st.write(
    "Upload a real estate legal document and analyze it using NLP and Transformers."
)

# ==========================================
# Upload PDF
# ==========================================

uploaded_file = st.file_uploader(
    "📄 Upload a PDF Document",
    type=["pdf"]
)

# ==========================================
# Process Uploaded PDF
# ==========================================

if uploaded_file is not None:

    st.success("✅ PDF Uploaded Successfully!")

    st.write("**File Name:**", uploaded_file.name)
    st.write("**File Size:**", round(uploaded_file.size / 1024, 2), "KB")

    # Save uploaded PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    # Read PDF
    text = read_pdf(temp_path)

    # ==========================================
    # View Extracted Text
    # ==========================================

    with st.expander("📄 View Extracted Text"):

        st.text_area(
            "PDF Content",
            text,
            height=350
        )

    # ==========================================
    # NER
    # ==========================================

    entities = extract_entities(text[:1000])

    result = organize_entities(entities)

    # ==========================================
    # Summary
    # ==========================================

    with st.spinner("Generating Summary..."):
        summary = summarize_document(text)

    # ==========================================
    # Risk Detection
    # ==========================================

    risks = detect_risks(text)

    # ==========================================
    # Two Column Layout
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📌 Extracted Information")

        for key, value in result.items():

            if value:
                st.write(f"**{key}:** {', '.join(value)}")
            else:
                st.write(f"**{key}:** None")

    with col2:

        st.subheader("⚠ Risk Detection")

        if len(risks) == 0:
            st.success("✅ No Risks Detected")
        else:
            for risk in risks:
                st.warning(risk)

    # ==========================================
    # Summary
    # ==========================================

    st.subheader("📝 Document Summary")

    st.success(summary)

    # ==========================================
    # Question Answering
    # ==========================================

    st.subheader("❓ Ask Questions")

    question = st.text_input(
        "Enter your question",
        placeholder="Example: Who is the seller?"
    )

    if st.button("Get Answer"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            with st.spinner("Finding answer..."):

                answer = answer_question(question, text)

            st.success("Answer")

            st.info(answer)

# ==========================================
# Footer
# ==========================================

st.markdown("---")

st.caption(
    "Developed using Python • Streamlit • Transformers • NLP"
)
