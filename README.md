# OCR_iLovePDF

Automated Optical Character Recognition (OCR) using the iLovePDF API.

![Project Demo](demo.gif) <!-- Replace with a screenshot, GIF, or video -->

## Table of Contents

- [Introduction](#introduction)
- - [Splitting PDFs](#splitting-pdfs)
- - [OCR and Processing](#ocr-and-processing)
- [Usage](#usage)
- [Combining OCR'ed PDFs](#combining-ocr'ed-pdfs)


## Introduction

OCR_iLovePDF is a Python script designed to automate the process of Optical Character Recognition (OCR) for PDF files using the iLovePDF. It handles splitting larger PDF files, performing OCR, and saving the processed OCR files.


### Splitting PDFs

The script automatically splits PDF files into smaller 10-page segments to meet iLovePDF's 15MB size limit for OCR processing.

### OCR and Processing

Processed OCR files are saved in the `ocred/pdf_name/` directory, organized by the splitted page numbers.

## Usage
python3 req.py -dir /absolute/path/to/directory/with/pdf/files

### Combining OCR'ed PDFs
To combine the processed OCR PDFs from the ocred directory:

python3 combine_files.py /path/to/ocred/file/directory
