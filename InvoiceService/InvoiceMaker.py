import os
import shutil
import textwrap
import openpyxl
import PyPDF2
import sys

import DataTypes
import Logger
import FileUtil as file

from datetime import datetime
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
sys.path.append(".")

 # Has support for: Client info sent via Customer class (company or person)
 # Support for multiple product sent by OrderedProducList class 

def MakeInvoice(customer, products, shippingCost):
    """Makes an invoice using DataTypes::Customer class, 
    DatTypes::OrderedProducList class and shippingCost - a int
    There can only be one client, but the products can be many.
    """
    NEW_LINE_11 = 15
    NEW_LINE_9 = 12    
    UM_0 = 'buc'

    if(shippingCost > 0):
        HAS_SHIPPING = True
    else:
        HAS_SHIPPING = False

    pdfmetrics.registerFont(TTFont('HelveticaNeue', 'HelveticaNeueCyr-Light.ttf'))

    # get invoice series
    invoiceSeries = file.getInvoiceSeries()
    
    print("Invoice series: ", invoiceSeries)
    Logger.Log("{}: {} {}".format(__name__,"Invoice series: ", invoiceSeries))

    # get invoice number
    invoiceNumber = file.getInvoiceNumber()
    
    print("Invoice number: ", invoiceNumber)
    Logger.Log("{}: {} {}".format(__name__, "Invoice number: ", invoiceNumber))

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
    Logger.Log("{}: {} {}".format(__name__, 'Current Timestamp : ', timestampStr))

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
            y = y - NEW_LINE_11
    else:
        y = 629
        for a in splitedAddr:
            can.drawString(380, y, a)
            y = y - NEW_LINE_11

    PRICE_X_INDENT_MOST_RIGHT = 555
    OOB_PRODUCT_Y_INDENT = 240
    can.setFontSize(9)
    ySubstractor = 0
    y = 456  
    finalPrice = []
    totalPrice = 0

    for it in range(0,len(products.productName)):
        splitedProductName = textwrap.fill(products.productName[it], 50).split('\n')
        indent = y
        Xindent = 73
        prettySpace = 0
        for a in splitedProductName:
            if(prettySpace > 0):
                Xindent = 75 
            else:
                Xindent = 73
            can.drawString(Xindent, indent, a)
            indent = indent - NEW_LINE_9
            ySubstractor = ySubstractor + 1 
            prettySpace = prettySpace + 1
        can.drawRightString(470, y, str(products.productPrice[it]))
        can.drawString(350, y, str(products.productQuantity[it]))
        can.drawString(295, y, UM_0)  

        # multiply quantiy with price
        finalPrice.insert(it, products.productQuantity[it] * products.productPrice[it])
        can.drawRightString(PRICE_X_INDENT_MOST_RIGHT, y, str(finalPrice[it]))
        y = y - ySubstractor * NEW_LINE_9 - 2
        if(OOB_PRODUCT_Y_INDENT > y):
            print("ERROR: There are too many products for this Invoice template!")
            Logger.Log("{}: {}".format(__name__, "ERROR: There are too many products for this Invoice template!"))
            break
        
    can.setFontSize(11)
    for it in finalPrice:
        totalPrice = totalPrice + it

    if(HAS_SHIPPING):
        can.drawRightString(PRICE_X_INDENT_MOST_RIGHT, 221, str(shippingCost))
        totalPrice = totalPrice + shippingCost
    
    #draw subtotal
    can.drawRightString(PRICE_X_INDENT_MOST_RIGHT, 201, str(totalPrice))
    #draw total sum
    can.setFontSize(12)
    can.drawRightString(PRICE_X_INDENT_MOST_RIGHT, 178, str(totalPrice))

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

    # increment the invoice number
    file.incrementInvoiceNumber()
