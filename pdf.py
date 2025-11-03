import os
import pytesseract
from pdf2image import convert_from_path

# ---------- CONFIG ----------
pdf_folder = r"D:\Python_OCR_Project\images\ScannedPdf"  # Folder with all PDFs D:\Python\Python_OCR_Project\images
poppler_path = r"D:\Program Files\poppler-25.07.0\Library\bin"  # Poppler bin path
output_folder = os.path.join(pdf_folder, "OCR_text")  # Save all OCR text here
os.makedirs(output_folder, exist_ok=True)
# ----------------------------

# Get all PDF files in the folder
pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]

if not pdf_files:
    print("⚠️ No PDF files found in the folder!")
else:
    print(f"Found {len(pdf_files)} PDF(s): {pdf_files}")

# Process each PDF
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    pdf_filename = os.path.splitext(pdf_file)[0]
    txt_filename = f"{pdf_filename}_ocr.txt"
    txt_path = os.path.join(output_folder, txt_filename)

    print(f"\n📄 Processing: {pdf_file}")

    try:
        # Convert PDF pages to images
        pages = convert_from_path(pdf_path, 300, poppler_path=poppler_path)

        # Extract text from all pages
        text = ""
        for i, page in enumerate(pages, start=1):
            page_text = pytesseract.image_to_string(page)
            text += f"\n\n--- Page {i} ---\n\n{page_text}"

        # Save extracted text to a file
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"✅ OCR complete! Text saved to: {txt_path}")

    except Exception as e:
        print(f"❌ Error processing {pdf_file}: {e}")

print("\n🎯 All PDFs processed successfully!")
