import PyPDF2
from PyPDF2 import PdfReader
import sys
import os

path = "/pdfs/"
filename = "CombinedPDFs.pdf"
# merger = PyPDF2.PdfFileMerger()
merger = PyPDF2.PdfMerger()

print("path: ", os.curdir)
for file in os.listdir(os.curdir + path):
    print(os.curdir + path)
    if file == "CombinedPDFs.pdf":
        print("Skipping:", file)
    elif file.endswith(".pdf"):
        print("Adding:", file)
        # merger.append(file)
        merger.append(file)

merger.write(os.curdir + path + filename)
