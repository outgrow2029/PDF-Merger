import os
from pypdf import PdfWriter

def merge_pdfs(output_name, *input_files):
    merger = PdfWriter()

    for pdf in input_files:
        print(f"Adding: {pdf}")
        merger.append(pdf)

    merger.write(output_name)
    merger.close()
    print(f"Success! Created: {output_name}")

# Usage:
# List your files in the order you want them merged
merge_pdfs("final_document.pdf", "file1.pdf", "file2.pdf")