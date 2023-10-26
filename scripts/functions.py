# import module

from external_libraries import *

def pdf_2_image(pdf_path: str):
    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_path, poppler_path=os.getcwd() + "\\poppler-23.10.0\\Library\\bin")

    for i in range(len(images)):
        # Save pages as images in the pdf
        assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'file_output_image\page'))
        images[i].save(assets_dir + str(i) + '.jpg', 'JPEG')

def image_2_text(path_to_tesseract : str, image_path : str ):


    # Opening the image & storing it in an image object
    img = Image.open(image_path)

    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract

    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)

    # Displaying the extracted text
    return text[:-1]



######### colocar spacy para dentro desse código

if __name__=='__main__':

    path_to_tesseract = r"C:\Users\sidneyd\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'file_output_image\page'))
    image_path = assets_dir + "11.jpg"
    print(image_2_text(path_to_tesseract, image_path))