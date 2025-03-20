# ZIP - Compressing / Decompressing files using zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Paths
ROOT_PATH = Path(__file__).parent
ZIP_DIR_PATH = ROOT_PATH / 'lesson186_zip_directory'
COMPRESSED_PATH = ROOT_PATH / 'lesson186_compressed.zip'
EXTRACTED_PATH = ROOT_PATH / 'lesson186_extracted'

# Clean up previous files/directories if they exist
shutil.rmtree(ZIP_DIR_PATH, ignore_errors=True)
Path.unlink(COMPRESSED_PATH, missing_ok=True)
shutil.rmtree(str(COMPRESSED_PATH).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(EXTRACTED_PATH, ignore_errors=True)

# Create directory for this example
ZIP_DIR_PATH.mkdir(exist_ok=True)


def create_files(quantity: int, zip_dir: Path):
    for i in range(quantity):
        text = f'file_{i}'
        with open(zip_dir / f'{text}.txt', 'w', encoding='utf-8') as file:
            file.write(text)


create_files(10, ZIP_DIR_PATH)

# Creating a ZIP file and adding files into it
with ZipFile(COMPRESSED_PATH, 'w') as zip_file:
    for root, dirs, files in os.walk(ZIP_DIR_PATH):
        for file in files:
            zip_file.write(os.path.join(root, file), file)

# Listing files inside the ZIP archive
with ZipFile(COMPRESSED_PATH, 'r') as zip_file:
    for file_name in zip_file.namelist():
        print(file_name)

# Extracting files from the ZIP archive
with ZipFile(COMPRESSED_PATH, 'r') as zip_file:
    zip_file.extractall(EXTRACTED_PATH)
