import sys
sys.path.append('C:\\Users\\daniel.cortes\\development\\git\\apeiron-cli\\apeiron-cli\\reader')

import reader

from fpdf import FPDF
 
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
pdf.output("simple_demo.pdf")

print(reader.add(2,3))