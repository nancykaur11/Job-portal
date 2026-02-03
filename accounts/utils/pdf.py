from pypdf import PdfReader

def extract_text_from_pdf(file_obj):
    reader = PdfReader(file_obj)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    file_obj.seek(0)
    return text
