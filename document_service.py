from io import BytesIO
from docx import Document


def format_docx(text: str):
    document = Document()

    for paragraph in text.split("\n"):
        document.add_paragraph(paragraph)

    output = BytesIO()
    document.save(output)
    output.seek(0)

    return output.getvalue()
