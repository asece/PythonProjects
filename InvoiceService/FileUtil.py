import InvoiceMaker
import openpyxl
import DataTypes
import Logger

def getInvoiceNumber():
    invoiceNumberFile = open("invoice_number.txt", "r")
    invoiceNumber = invoiceNumberFile.readline()
    invoiceNumberFile.close()
    print("Read invoice number: ", invoiceNumber)
    Logger.Log("{}: {} {}".format(__name__, "Read invoice number: ", invoiceNumber))
    return invoiceNumber

def incrementInvoiceNumber():
    invoiceNumberFile = open("invoice_number.txt", "r")
    invoiceNumber = invoiceNumberFile.readline()
    invoiceNumberFile.close()

    invoiceNumberFile = open("invoice_number.txt", "w")  
    newInvoiceNumber = int(invoiceNumber)
    newInvoiceNumber = newInvoiceNumber + 1
    invoiceNumberFile.write(str(newInvoiceNumber))
    invoiceNumberFile.close()
    print("Wrote new invoice number: ", newInvoiceNumber)
    Logger.Log("{}: {} {}".format(__name__, "Wrote new invoice number: ", newInvoiceNumber))

def getInvoiceSeries():
    invoiceSeriesFile = open("invoice_series.txt","r")
    invoiceSeries = invoiceSeriesFile.readline()
    invoiceSeriesFile.close()
    print("Read invoice series: ", invoiceSeries)
    Logger.Log("{}: {} {}".format(__name__, "Read invoice series: ", invoiceSeries))
    return invoiceSeries