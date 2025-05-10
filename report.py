from fpdf import FPDF

def create_pdf_report(question, answer, context, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, f"Domanda: {question}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Risposta: {answer}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Contesto usato:\n{context}")

    pdf.output(filename)