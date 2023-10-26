# import module
from pdf2image import convert_from_path
import os

# Store Pdf with convert_from_path function
images = convert_from_path('pibgo2002.pdf', poppler_path=os.getcwd() + "\\poppler-23.10.0\\Library\\bin")

for i in range(len(images)):
    # Save pages as images in the pdf
    images[i].save('file_output_image\page' + str(i) + '.jpg', 'JPEG')