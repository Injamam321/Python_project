import docx
from PyPDF2 import PdfReader

def pdf_to_word(pdf_path, word_path):
    '''
    Convert a PDF file to a Word document.
    
    :param pdf_path: path to the PDF file
    :param word_path: path to the Word document
    '''

    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            pdf_pages = len(pdf_reader.pages)

            # Create a new Word document
            doc = docx.Document()

            # Loop through all pages of the PDF and write them to the Word file
            for i in range(pdf_pages):
                pdf_page = pdf_reader.pages[i]
                text = pdf_page.extract_text()
                if text:  # Ensure the page has text before adding
                    doc.add_paragraph(text)

            # Save the Word document
            doc.save(word_path)
            print("Your PDF has been successfully converted to Word.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
pdf_path = 'example.pdf'
word_path = 'example.docx'

pdf_to_word(pdf_path, word_path)
