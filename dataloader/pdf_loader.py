import PyPDF2
import os
from constants import FILE_TYPE, CHUNK_SIZE
from typing import List


pdf_folder_path = "../domain_retrieval/"

def chunker(text_data: List[str]):
    chunks = [text[]]

def retrieve_data(parent_folder: str) -> List[str]:
    text_data = []
    for pdf_file in os.listdir(parent_folder):
        if not pdf_file.endswith(FILE_TYPE):
            continue
        with open(os.path.join(parent_folder, pdf_file), 'rb') as file:
            print(pdf_file)
            reader = PyPDF2.PdfReader(os.path.join(parent_folder, pdf_file))
            text = ""
            for page_number in range(len(reader.pages)):
                page = reader.pages[page_number]
                text += page.extract_text()
        text_data.append(text)
    return text_data

print(retrieve_data(pdf_folder_path))
