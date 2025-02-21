import argparse
from pypdf import PdfMerger

def merge_pdfs(pdf_list, output_filename):
    merger = PdfMerger()
    
    for pdf in pdf_list:
        merger.append(pdf)
    
    merger.write(output_filename)
    merger.close()
    print(f"✅ Successfully merged PDFs into '{output_filename}'!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge multiple PDF files into one.")
    parser.add_argument("pdfs", nargs="+", help="List of PDF files to merge")
    parser.add_argument("-o", "--output", default="merged.pdf", help="Output PDF filename (default: merged.pdf)")

    args = parser.parse_args()
    merge_pdfs(args.pdfs, args.output)
