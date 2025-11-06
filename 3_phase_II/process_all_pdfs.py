#!/usr/bin/env python3
"""
Script to extract text from all PDFs in 'pdf included' folder
and create corresponding .md files.
"""
import os
from pathlib import Path
import sys

# Import the extraction function
sys.path.insert(0, os.path.dirname(__file__))
from extract_pdf_text import extract_pdf_text

def process_all_pdfs():
    """Process all PDFs in the 'pdf included' folder."""
    pdf_dir = Path("pdf included")
    output_dir = Path(".")
    
    if not pdf_dir.exists():
        print(f"Error: Directory '{pdf_dir}' not found", file=sys.stderr)
        return
    
    pdf_files = sorted(pdf_dir.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in '{pdf_dir}'", file=sys.stderr)
        return
    
    print(f"Found {len(pdf_files)} PDF files to process\n", file=sys.stderr)
    
    success_count = 0
    failed_count = 0
    
    for pdf_file in pdf_files:
        # Create output filename: remove .pdf extension and add .md
        output_file = output_dir / (pdf_file.stem + ".md")
        
        print(f"Processing: {pdf_file.name} -> {output_file.name}...", file=sys.stderr, end=" ")
        
        try:
            text = extract_pdf_text(pdf_file)
            
            if text and text.strip():
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(text)
                print("✓", file=sys.stderr)
                success_count += 1
            else:
                print("✗ (no text extracted)", file=sys.stderr)
                failed_count += 1
        except Exception as e:
            print(f"✗ (error: {e})", file=sys.stderr)
            failed_count += 1
    
    print(f"\nCompleted: {success_count} successful, {failed_count} failed", file=sys.stderr)

if __name__ == '__main__':
    process_all_pdfs()

