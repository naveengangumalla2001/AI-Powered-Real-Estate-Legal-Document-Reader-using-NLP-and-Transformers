# Professional Streamlit UI template
# Replace your current streamlit_app.py with this file.

import streamlit as st
import tempfile
import time

from pdf_reader import read_pdf
from ner import extract_entities
from entity_formatter import organize_entities
from summarizer import summarize_document
from question_answer import answer_question
from risk_detector import detect_risks

st.set_page_config(page_title="AI Real Estate Legal Document Reader", page_icon="🏠", layout="wide")

st.sidebar.title("🏠 AI Document Reader")
st.sidebar.markdown("### Features")
st.sidebar.markdown("- 📄 PDF Upload\n- 🔍 Text Extraction\n- 🤖 BERT NER\n- 📝 BART Summary\n- ⚠ Risk Detection\n- ❓ Question Answering")
st.sidebar.markdown("---")
st.sidebar.info("Developed by **Naveen Kumar**")

st.title("🏠 AI-Powered Real Estate Legal Document Reader")
uploaded_file = st.file_uploader("📄 Upload PDF", type=["pdf"])

if uploaded_file:
    start = time.time()

    c1,c2,c3 = st.columns(3)
    c1.metric("File", uploaded_file.name)
    c2.metric("Size (KB)", round(uploaded_file.size/1024,2))
    c3.metric("Type","PDF")

    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as f:
        f.write(uploaded_file.read())
        path = f.name

    progress = st.progress(0)
    progress.progress(10)
    text = read_pdf(path)
    progress.progress(30)
    entities = extract_entities(text[:1000])
    progress.progress(50)
    result = organize_entities(entities)
    progress.progress(70)
    summary = summarize_document(text)
    progress.progress(90)
    risks = detect_risks(text)
    progress.progress(100)

    st.success("Analysis Completed")

    a,b,c = st.columns(3)
    a.metric("Words", len(text.split()))
    b.metric("Characters", len(text))
    c.metric("Pages", max(1,text.count("\f")+1))

    with st.expander("View Extracted Text"):
        st.text_area("Text", text, height=300)

    l,r = st.columns(2)

    with l:
        st.subheader("Entities")
        for k,v in result.items():
            st.write("**"+k+"**")
            if v:
                for i in v:
                    st.write("•",i)
            else:
                st.write("None")

    with r:
        st.subheader("Risk Analysis")
        if risks:
            for risk in risks:
                st.error(risk)
        else:
            st.success("No risks detected")

    st.subheader("Summary")
    st.text_area("Generated Summary", summary, height=180)

    q = st.text_input("Ask a question")
    if st.button("Get Answer") and q.strip():
        st.info(answer_question(q,text))

    report = f"SUMMARY\n\n{summary}\n\nRISKS\n\n" + ("\n".join(risks) if risks else "No risks detected")

    st.download_button("📥 Download Analysis Report", report, file_name="analysis_report.txt")

    st.success(f"Processing Time: {time.time()-start:.2f} seconds")

st.markdown("---")
st.caption("Built with Python • Streamlit • Transformers • NLP")
