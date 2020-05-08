import os
import shutil
import textwrap
import openpyxl
import PyPDF2
import sys

import DataTypes

from datetime import datetime
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
sys.path.append(".")

def TestMe(rcvClass):
    print(rcvClass)

def MakeInvoice(products, customer):
    NEWLINE_DISTANCE = 15

    pdfmetrics.registerFont(TTFont('HelveticaNeue', 'HelveticaNeueCyr-Light.ttf'))

    # get invoice series
    invoiceSeriesFile = open("invoice_series.txt","r")
    invoiceSeries = invoiceSeriesFile.readline()
    invoiceSeriesFile.close()
    print("Invoice series: ", invoiceSeries)

    # get invoice number
    invoiceNumberFile = open("invoice_number.txt", "r")
    invoiceNumber = invoiceNumberFile.readline()
    invoiceNumberFile.close()
    print("Invoice number: ", invoiceNumber)

    # update invoice number
    invoiceNumberFile = open("invoice_number.txt", "w")
    newNr = int(invoiceNumber)
    newNr = newNr + 1
    invoiceNumberFile.write(str(newNr))
    invoiceNumberFile.close()
    print("New invoice number: ", newNr)

    #make a copy of the invoice to work with
    src_dir="blank_invoice.pdf"
    dst_dir="Invoice.pdf"
    shutil.copy(src_dir,dst_dir)

    # create a new PDF with Reportlab
    can = canvas.Canvas("TextToAdd.pdf", pagesize=A4)
    can.setFont('HelveticaNeue', 11)

    # add serial and number
    serialAndDate = "Seria "+ invoiceSeries + " nr " + invoiceNumber
    can.drawString(283, 711, serialAndDate)

    # add the current date
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%m-%Y")
    can.drawString(291, 696, timestampStr)
    print('Current Timestamp : ', timestampStr)

    # format the address to fit in the document
    wAddr = textwrap.fill(customer.address, 35)
    splitedAddr = wAddr.split('\n')
    print(wAddr)

    # add client info
    can.drawString(380, 654, customer.name)
    if(customer.isCompany):
        CUI = "CUI: " + str(customer.CUI)
        Inreg = "Nr. Inreg: " + str(customer.nrInreg)
        can.drawString(380, 639, CUI)
        can.drawString(380, 624, Inreg)
        y = 599
        for a in splitedAddr:
            can.drawString(380, y, a)
            y = y - 15
    else:
        y = 629
        for a in splitedAddr:
            can.drawString(380, y, a)
            y = y - 15

    # format product name to fit in the document
    print(textwrap.fill(products.productName[0], 35))

    splitedProductName = textwrap.fill(products.productName[0], 50).split('\n')

    # add 1 product
    # TODO : Add support for several products !
    # TODO : Implement total sum calculation 

    y = 456
    for a in splitedProductName:
        can.setFontSize(9)
        can.drawString(73, y, a)
        y = y - 12
    #can.drawString(450, 456, str(products.productPrice[0]))
    can.setFontSize(10)
    
    can.drawRightString(470, 456, str(products.productPrice[0]))


    can.setFontSize(10)

    # save the canvas 
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