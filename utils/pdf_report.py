from fpdf import FPDF

def generate_pdf(pest, confidence, severity, treatment, crop_loss):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", "B", 16)

    pdf.cell(200, 10, "AI Pest Detection Report", ln=True, align="C")

    pdf.ln(10)

    pdf.set_font("Arial", "", 12)

    pdf.cell(200, 10, f"Detected Pest : {pest}", ln=True)

    pdf.cell(200, 10, f"Confidence : {confidence} %", ln=True)

    pdf.cell(200, 10, f"Severity : {severity}", ln=True)

    pdf.cell(200, 10, crop_loss, ln=True)

    pdf.ln(5)

    pdf.multi_cell(0, 10, "Organic Treatment:\n"+treatment["organic"])

    pdf.ln(3)

    pdf.multi_cell(0, 10, "Chemical Treatment:\n"+treatment["chemical"])

    pdf.ln(3)

    pdf.multi_cell(0, 10, "Prevention:\n"+treatment["prevention"])

    pdf.output("Pest_Report.pdf")