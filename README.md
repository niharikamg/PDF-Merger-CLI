# PDF Merger CLI

## Description
The **PDF Merger CLI** is a simple command-line tool that allows users to merge multiple PDF files into a single document. It supports specifying the order of files and naming the output file.

## Features
- Merge multiple PDF files into one.
- Specify the order of PDFs.
- Provide an optional output filename.
- Simple and lightweight.

## Requirements
Ensure you have **Python 3.6+** installed. Additionally, install the required library:
```sh
pip install pypdf
```

## Usage
Run the script with the following command:
```sh
python pdf_merger.py file1.pdf file2.pdf file3.pdf -o merged_output.pdf
```
- If you don't specify an output file, it defaults to `merged.pdf`:
```sh
python pdf_merger.py file1.pdf file2.pdf
```

## Example
### Before:
- `document1.pdf`
- `document2.pdf`
- `document3.pdf`

### After running:
```sh
python pdf_merger.py document1.pdf document2.pdf document3.pdf -o final_merged.pdf
```
You get: **final_merged.pdf** (containing all pages from the input PDFs).

## How It Works
1. The script reads all the input PDFs.
2. It merges them in the specified order.
3. The merged file is saved with the given name.
4. A success message is displayed.

## Future Enhancements
- Add a GUI version.
- Include a page selection feature.
- Allow drag & drop functionality.

## Contributing
Feel free to submit pull requests and improve the project!


