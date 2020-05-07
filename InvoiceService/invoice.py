import os
import shutil

import openpyxl
import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

#make a copy of the invoice to work with
src_dir="blank_invoice.pdf"
dst_dir="Invoice.pdf"
shutil.copy(src_dir,dst_dir)

#import the sheets from the excel file
try:
    clientTable = openpyxl.load_workbook('client_info.xlsx')
    clientSheet = clientTable['clients']
except:
    print("Could not access the Client Table! Shutting down!")
    raise SystemExit
try:
    productTable = openpyxl.load_workbook('product_info.xlsx')
    productSheet = productTable['products']
except:
    print("Could not access the Product Table! Shutting down!")
    raise SystemExit

#Page information
page_width = 2156
page_height = 3050

class CompanyClient:
    CUI = ''
    Inreg = ''


def checkIfCompany(field):
    if(field == "x"):
        return True
    else:
        return False


customer = clientSheet.cell(row = 2, column = 1).value
print(customer, end='  ')
if(checkIfCompany(clientSheet.cell(row = 2, column = 2).value)):
    company = CompanyClient()
    company.CUI = clientSheet.cell(row = 2, column = 3).value
    company.Inreg = clientSheet.cell(row = 2, column = 4).value
    print(company.CUI, company.Inreg, end='  ')
address = clientSheet.cell(row = 2, column = 5).value
print(address)

productId = productSheet.cell(row = 2, column = 1).value
productName = productSheet.cell(row = 2, column = 2).value
productPrice = productSheet.cell(row = 2, column = 3).value

print(productId, ' ', productName, ' ', productPrice)


# create a new PDF with Reportlab
can = canvas.Canvas("TextToAdd.pdf", pagesize=A4)
can.drawString(270, 695, "Seria FAS Nr 11")
can.save()



new_pdf = PdfFileReader('TextToAdd.pdf')
existing_pdf = PdfFileReader("Invoice.pdf")

output = PdfFileWriter()

page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("ClientInvoice.pdf", "wb")
output.write(outputStream)
outputStream.close()