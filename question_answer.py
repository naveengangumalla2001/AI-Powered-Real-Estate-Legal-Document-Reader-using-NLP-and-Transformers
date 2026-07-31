from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

def answer_question(question, context):

    result = qa_pipeline(
        question=question,
        context=context[:3000]   # Use first 3000 characters
    )

    return result["answer"]