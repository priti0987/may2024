import PyPDF2
import os

os.chdir("C:\\Users\\Dell\\Documents\\MyDocs2024Ascendion")
pdfFile = open('tax_computation_12_2023.pdf','rb')
reader = PyPDF2.PdfReader(pdfFile)
print(len(reader.pages))

page = reader.pages[0]
print(page.extract_text())