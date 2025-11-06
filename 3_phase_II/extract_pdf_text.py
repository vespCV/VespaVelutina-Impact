#!/usr/bin/env python3
"""
Script to extract text from PDF files and save as markdown files.
Tries multiple PDF extraction libraries.
"""
import sys
import os
from pathlib import Path

def extract_with_pypdf2(pdf_path):
    """Extract text using PyPDF2."""
    try:
        import PyPDF2
        text = []
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text.append(page.extract_text())
        return '\n'.join(text)
    except ImportError:
        return None
    except Exception as e:
        print(f"Error with PyPDF2: {e}", file=sys.stderr)
        return None

def extract_with_pdfplumber(pdf_path):
    """Extract text using pdfplumber."""
    try:
        import pdfplumber
        text = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text.append(page.extract_text() or '')
        return '\n'.join(text)
    except ImportError:
        return None
    except Exception as e:
        print(f"Error with pdfplumber: {e}", file=sys.stderr)
        return None

def extract_pdf_text(pdf_path):
    """Extract text from PDF using available library."""
    # Try pdfplumber first (better quality)
    text = extract_with_pdfplumber(pdf_path)
    if text:
        return text
    
    # Try PyPDF2 as fallback
    text = extract_with_pypdf2(pdf_path)
    if text:
        return text
    
    return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 extract_pdf_text.py <pdf_file> [output_file]")
        sys.exit(1)
    
    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)
    
    output_path = sys.argv[2] if len(sys.argv) > 2 else pdf_path.with_suffix('.md')
    
    print(f"Extracting text from {pdf_path.name}...", file=sys.stderr)
    text = extract_pdf_text(pdf_path)
    
    if text:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Successfully extracted to {output_path}", file=sys.stderr)
        sys.exit(0)
    else:
        print("Error: Could not extract text. No PDF libraries available.", file=sys.stderr)
        sys.exit(1)

