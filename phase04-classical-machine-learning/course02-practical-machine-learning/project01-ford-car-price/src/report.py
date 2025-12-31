from fpdf import FPDF
from pathlib import Path

class PDFReport:
    def __init__(self, title="Ford Project Report"):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.title = title

    def add_title(self):
        self.pdf.add_page()
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(0, 10, self.title, ln=True, align="C")

    def add_section(self, heading):
        self.pdf.set_font("Arial", "B", 14)
        self.pdf.ln(10)
        self.pdf.cell(0, 10, heading, ln=True)

    def add_text(self, text):
        self.pdf.set_font("Arial", "", 12)
        self.pdf.multi_cell(0, 8, text)

    def add_image(self, image_path, w=180):
        image_path = Path(image_path)
        if image_path.exists():
            self.pdf.image(str(image_path), w=w)
        else:
            self.add_text(f"Image not found: {image_path}")

    def save(self, path):
        self.pdf.output(str(path))
