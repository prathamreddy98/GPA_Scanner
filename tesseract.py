import pytesseract
from PIL import Image
import fitz
import re
import os
from os import listdir
    
def pdf_to_images(pdf_path, output_folder, dpi = 300):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate over each page in the PDF
    for page_number in range(len(pdf_document)):
        # Get the page
        page = pdf_document.load_page(page_number)

        # Convert the page to an image
        zoom_factor = dpi/72.0
        pix = page.get_pixmap(matrix = fitz.Matrix(zoom_factor, zoom_factor))
        image_path = f"{output_folder}/page_{page_number + 1}.png"

        # Save the image
        pix.save(image_path)
        print(f"Page {page_number + 1} saved as {image_path}")

    # Close the PDF document
    pdf_document.close()

# Path to the PDF file
pdf_path = "TranscriptUnoff.pdf"

# Output folder for images
output_folder = "output_images"


# Convert PDF to images
pdf_to_images(pdf_path, output_folder)


# Path to your image file

for images in os.listdir(output_folder):
    
	image_path = 'output_images/' + images
	image = Image.open(image_path)

	# Perform OCR using pytesseract
	text = pytesseract.image_to_string(image)

	# Print the extracted text
	# print("Extracted Text:")
	# print(type(text))
	with open("output.txt", 'w') as file:
		file.write(text)

	def find_cgpa(text):
		# Regular expression pattern to match CGPA
		pattern = r'\b\d+\.\d{3}\b'

		# Find all occurrences of CGPA in the text
		cgpa_values = re.findall(pattern, text)

		return cgpa_values
	print(find_cgpa(text))