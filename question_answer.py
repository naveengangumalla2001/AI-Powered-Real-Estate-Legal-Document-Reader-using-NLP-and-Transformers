import re
from transformers import pipeline

# ------------------------------------------
# Load Question Answering Model
# ------------------------------------------

qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

# ------------------------------------------
# Regex Helper Functions
# ------------------------------------------

def extract_witnesses(text):

    pattern = r"WITNESSES?:\s*(.*)"

    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

    if match:
        witness_text = match.group(1)
        witness_text = witness_text.split("\n\n")[0]
        return witness_text.strip()

    return None


def extract_money(text):

    pattern = r"Rs\.?\s?[\d,]+/?-?"

    money = re.findall(pattern, text)

    if money:
        return ", ".join(money)

    return None


def extract_date(text):

    pattern = r"\d{1,2}(?:st|nd|rd|th)?\s+(?:day\s+of\s+)?[A-Za-z]+,\s+\d{4}"

    dates = re.findall(pattern, text)

    if dates:
        return ", ".join(dates)

    return None


def extract_document_number(text):

    pattern = r"Document No\.?\s*[:.]?\s*([\w/-]+)"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group(1)

    return None


def extract_plot_number(text):

    pattern = r"Plot No\.?\s*([\w/-]+)"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group(1)

    return None


# ------------------------------------------
# Main QA Function
# ------------------------------------------

def answer_question(question, context):

    q = question.lower()

    # -----------------------------
    # Witnesses
    # -----------------------------

    if "witness" in q:

        answer = extract_witnesses(context)

        if answer:
            return answer

    # -----------------------------
    # Money
    # -----------------------------

    if "amount" in q or "price" in q or "money" in q or "sale consideration" in q:

        answer = extract_money(context)

        if answer:
            return answer

    # -----------------------------
    # Date
    # -----------------------------

    if "date" in q:

        answer = extract_date(context)

        if answer:
            return answer

    # -----------------------------
    # Document Number
    # -----------------------------

    if "document number" in q or "registration number" in q:

        answer = extract_document_number(context)

        if answer:
            return answer

    # -----------------------------
    # Plot Number
    # -----------------------------

    if "plot" in q:

        answer = extract_plot_number(context)

        if answer:
            return answer

    # -----------------------------
    # Otherwise use DistilBERT
    # -----------------------------

    result = qa_pipeline(
        question=question,
        context=context[:3000]
    )

    return result["answer"]
