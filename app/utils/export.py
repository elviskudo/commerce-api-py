import pandas as pd
from fastapi.responses import FileResponse

def export_to_csv(data, filename="export.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    return FileResponse(filename, media_type='text/csv', filename=filename)

def export_to_xls(data, filename="export.xls"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    return FileResponse(filename, media_type='application/vnd.ms-excel', filename=filename)

def export_to_pdf(data, filename="export.pdf"):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    textobject = c.beginText(40, height - 40)
    textobject.setFont("Helvetica", 12)

    for item in data:
        textobject.textLine(str(item))

    c.drawText(textobject)
    c.save()
    return FileResponse(filename, media_type='application/pdf', filename=filename)