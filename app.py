from utils.pdf_reader import read_pdf
from utils.ner import extract_entities
from utils.entity_formatter import organize_entities
from utils.summarizer import summarize_document
from utils.question_answer import answer_question
from utils.risk_detector import detect_risks

# ==========================================
# PDF Path
# ==========================================

pdf_path = "dataset/sale_agreements/sale_deed.pdf"

# Read PDF
text = read_pdf(pdf_path)

# ==========================================
# Step 4: Entity Extraction
# ==========================================

entities = extract_entities(text[:1000])
result = organize_entities(entities)

print("\n========== Extracted Information ==========\n")

for key, value in result.items():
    if value:
        print(f"{key}: {', '.join(value)}")
    else:
        print(f"{key}: None")

# ==========================================
# Step 5: Document Summarization
# ==========================================

print("\n========== Document Summary ==========\n")

summary = summarize_document(text)

print(summary)

# ==========================================
# Step 7: Risk Detection
# ==========================================

print("\n========== Risk Detection ==========\n")

risks = detect_risks(text)

if len(risks) == 0:
    print("✅ No risks detected.")
else:
    for risk in risks:
        print("⚠", risk)

# ==========================================
# Step 6: Question Answering
# ==========================================

print("\n========== Question Answering ==========\n")

while True:

    question = input("Ask a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("\nThank you for using the AI Document Reader!")
        break

    answer = answer_question(question, text)

    print("\nAnswer:")
    print(answer)
    print("-" * 50)