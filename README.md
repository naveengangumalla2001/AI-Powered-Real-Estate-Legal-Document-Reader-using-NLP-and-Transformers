# 🏠 AI-Powered Real Estate Legal Document Reader

## 📌 Project Overview

This project is an AI-powered web application that analyzes real estate
legal documents using **Natural Language Processing (NLP)** and
**Transformer models**.

Users can upload a PDF document and automatically:

-   📄 Extract text from the PDF
-   👤 Identify important entities (People, Locations, Organizations,
    etc.)
-   📝 Generate a document summary
-   ⚠️ Detect potential risks or missing information
-   ❓ Ask questions about the uploaded document

The application is built with **Python**, **Streamlit**, and **Hugging
Face Transformers**.

------------------------------------------------------------------------

## 🚀 Features

-   PDF Upload
-   PDF Text Extraction
-   Named Entity Recognition (NER)
-   Document Summarization
-   Risk Detection
-   Question Answering
-   Interactive Streamlit UI

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python
-   Streamlit
-   Hugging Face Transformers
-   BERT (NER)
-   BART (Summarization)
-   DistilBERT (Question Answering)
-   pdfplumber

------------------------------------------------------------------------

## 📂 Project Structure

``` text
RealEstate_Document_Reader/
│
├── dataset/
├── utils/
│   ├── pdf_reader.py
│   ├── ner.py
│   ├── entity_formatter.py
│   ├── summarizer.py
│   ├── risk_detector.py
│   └── question_answer.py
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

## ▶️ Installation

``` bash
git clone <your-repository-url>
cd RealEstate_Document_Reader
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Run the Application

``` bash
streamlit run streamlit_app.py
```

------------------------------------------------------------------------

## 📋 Workflow

1.  Upload a PDF
2.  Extract text
3.  Perform Named Entity Recognition
4.  Generate a summary
5.  Detect risks
6.  Ask questions about the document

------------------------------------------------------------------------

## 📸 Output

The application provides:

-   Extracted Text
-   Extracted Information
-   Document Summary
-   Risk Detection
-   Question Answering

------------------------------------------------------------------------

## 👨‍💻 Developed By

Naveen Kumar

Project: AI-Powered Real Estate Legal Document Reader
