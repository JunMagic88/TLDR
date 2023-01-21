# Converts epubs to txt files

from ebooklib import epub
import ebooklib
from bs4 import BeautifulSoup
import os
import PyPDF2 #importing PyPDF2 library

# Set the directory where the ePub files are located
input_dir = '00.EPUBs+PDFs'
output_dir = "Texts"

# run through each file in input folder
for filename in os.listdir(input_dir):
    full_text = ""

    # for each epub file
    if filename.endswith('.epub'):

        # get book title and content
        book = epub.read_epub(os.path.join(input_dir, filename))
        book_title = book.get_metadata('DC', 'title')[0][0]
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                html_content = item.get_content().decode('utf-8')
                soup = BeautifulSoup(html_content, 'html.parser')  
                text = soup.get_text()
                full_text += text
        
        # write to a txt file named after the book title
        txt_title = f"{book_title}.txt"
        with open(os.path.join(output_dir, txt_title), 'w') as f:
            f.write(full_text)
    
    # for each pdf file
    elif filename.endswith('.pdf'):
        pdf_file = open(os.path.join(input_dir, filename), 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in range(len(pdf_reader.pages)):
            page_obj = pdf_reader.pages[page]
            full_text += page_obj.extract_text()
        pdf_file.close()
        
        # write to a txt file named after the book title
        txt_title = f"{filename[:-4]}.txt"
        with open(os.path.join(output_dir, txt_title), 'w') as f:
            f.write(full_text)