# PyPDF2 for manipulating PDF files (PdfMerger)
# PyPDF2 is a pure Python library for manipulating PDF files,
# free and open-source. It can read, manipulate, write, and merge PDF data,
# add annotations, transform pages, extract text and images,
# manipulate metadata, and more.
# Documentation contains all the necessary information to use PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Activate your virtual environment
# pip install pypdf2

from pathlib import Path
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

ROOT_FOLDER = Path(__file__).parent
ORIGINAL_PDFS = ROOT_FOLDER / 'original_files'
NEW_FILES_FOLDER = ROOT_FOLDER / 'new_files'

BACEN_REPORT = ORIGINAL_PDFS / 'R20230210.pdf'

NEW_FILES_FOLDER.mkdir(exist_ok=True)

reader = PdfReader(BACEN_REPORT)

print(len(reader.pages))
for page in reader.pages:
    print(page)
    print()

page0 = reader.pages[0]
image0 = page0.images[0]

# print(page0.extract_text())
# with open(NEW_FILES_FOLDER / image0.name, 'wb') as fp:
#     fp.write(image0.data)

# Splitting each page into a separate PDF
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(NEW_FILES_FOLDER / f'page{i}.pdf', 'wb') as file:
        writer.add_page(page)
        writer.write(file)  # type: ignore

# Files to merge (in this case: pages 1 and 0 in reverse order)
files = [
    NEW_FILES_FOLDER / 'page1.pdf',
    NEW_FILES_FOLDER / 'page0.pdf',
]

# Merge PDFs
merger = PdfMerger()
for file in files:
    merger.append(file)  # type: ignore

merger.write(NEW_FILES_FOLDER / 'MERGED.pdf')  # type: ignore
merger.close()
