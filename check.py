from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def is_pdf_full_blank(file_path):
    manager = PDFResourceManager()
    output = StringIO()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    with open(file_path, "rb") as f:
        for page in PDFPage.get_pages(f):
            interpreter.process_page(page)

    text = output.getvalue().strip()
    converter.close()
    output.close()

    return text == ""

if __name__ == "__main__":
    file_path = "blank.pdf"
    if is_pdf_full_blank(file_path):
        print("The PDF file is full blank.")
    else:
        print("The PDF file is not full blank.")
