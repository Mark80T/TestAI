import os
from build_faiss import get_faiss_index, get_texts_from_db
from query_llm import ask_question
from report import create_pdf_report

print("Creazione nuovo indice FAISS...")
index, texts = get_faiss_index()

while True:
    question = input("\nInserisci la tua domanda (o 'exit' per uscire): ")
    if question.lower() == "exit":
        break
    answer, context = ask_question(question, index, texts)
    print(f"\nRisposta:\n{answer}")
    create_pdf_report(question, answer, context)