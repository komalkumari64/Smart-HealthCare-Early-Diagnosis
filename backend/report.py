from reportlab.pdfgen import canvas

def create_report():

    file = "analytics_report.pdf"

    pdf = canvas.Canvas(file)

    pdf.drawString(
        100,
        750,
        "Smart Healthcare Analytics Report"
    )

    pdf.save()

    return file