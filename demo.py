import PyPDF2
from PIL import Image

def is_same_color(image):
    # get the pixels of the image
    pixels = image.load()
    # get the first pixel color
    color = pixels[0, 0]
    # loop through all the pixels
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            # if the current pixel color is different from the first pixel color
            if pixels[i, j] != color:
                return False
    return True

# open the PDF file
pdf_file = open("blackss.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# loop through all the pages in the PDF
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    # get all the XObjects (which can include images) in the current page
    xobjects = page['/Resources']['/XObject'].getObject()
    # loop through all the XObjects in the current page
    for obj_key in xobjects:
        xobject = xobjects[obj_key]
        # check if the XObject is an image
        if xobject['/Subtype'] == '/Image':
            # get the image data from the XObject
            image_data = xobject.getData()
            # open the image
            image = Image.open(io.BytesIO(image_data))
            # check if the image is of the same color
            if is_same_color(image):
                print("Page", page_num + 1, ": Image is of the same color")
                break

pdf_file.close()
