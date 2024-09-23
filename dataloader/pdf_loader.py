import PyPDF2
import os
from constants import FILE_TYPE, CHUNK_SIZE
from typing import List

pdf_folder_path = "../domain_retrieval/"


def chunker(text: str) -> List[str]:
    chunks = [text[i:i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]
    return chunks


def retrieve_data(parent_folder: str = pdf_folder_path) -> List[str]:
    chunked_data = []
    for pdf_file in os.listdir(parent_folder):
        if not pdf_file.endswith(FILE_TYPE):
            continue
        with open(os.path.join(parent_folder, pdf_file), 'rb') as file:
            reader = PyPDF2.PdfReader(os.path.join(parent_folder, pdf_file))
            for page_number in range(len(reader.pages)):
                page = reader.pages[page_number]
                page_data = page.extract_text()
                page_chunk = chunker(page_data)
                chunked_data.extend(page_chunk)
    return chunked_data

# print(retrieve_data(pdf_folder_path)[0])
