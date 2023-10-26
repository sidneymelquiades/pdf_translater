# import module

from external_libraries import *

def pdf_2_image(pdf_path: str):
    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_path, poppler_path=os.getcwd() + "\\poppler-23.10.0\\Library\\bin")

    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save('file_output_image\page' + str(i) + '.jpg', 'JPEG')

if __name__=='__main__':
    pass