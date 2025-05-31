# text_extractor.py

import PyPDF2

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            with open("Selected_Document.txt", "w", encoding="utf-8") as f:
                f.write(text.strip())
            print("✅ PDF extraction successful.")
            return text
    except Exception as e:
        print("❌ Failed to extract text:", e)
        return ""

def main():
    pdf_path = "English_bulldog_genetics.pdf" 
    extract_text_from_pdf(pdf_path)

if __name__ == '__main__':
    main()
