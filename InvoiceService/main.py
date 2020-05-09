import InvoiceMaker
import openpyxl
import DataTypes
import Logger
import FileUtils as file

Products = file.getAllProducts()
Clients = file.getAllClients()

orderingClient = DataTypes.Customer()
orderedProds = DataTypes.OrderedProducList()

# Simulate an invoice creation
orderingClient.name = Clients.name[0]
orderingClient.CUI = Clients.CUI[0]
orderingClient.nrInreg = Clients.nrInreg[0]
orderingClient.address = Clients.address[0]
orderingClient.isCompany = Clients.isCompany[0]

orderedProds.productName.insert(0, Products.productName[0])
orderedProds.productPrice.insert(0, Products.productPrice[0])
orderedProds.productQuantity.insert(0, 2)

InvoiceMaker.MakeInvoice(orderedProds, orderingClient, 15)

#text = str(Products.productId[0]) + str(Products.productName[0]) + str(Products.productPrice[0])
#Logger.Log(text)

#InvoiceMaker.TestMe(orderedProducts)
#InvoiceMaker.MakeInvoice(orderedProducts, customerInfo, 55)
#file.getAllClients()
#file.getAllProducts()