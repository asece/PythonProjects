import InvoiceMaker
import DataTypes
import Logger
import FileUtil as file
import ExcellFileUtil as xlsx

#Products = xlsx.getAllProducts()
#Clients = xlsx.getAllClients()

#orderingClient = DataTypes.Customer()
#orderedProds = DataTypes.OrderedProducList()
#
## Simulate an invoice creation
#orderingClient.name = Clients.name[0]
#orderingClient.CUI = Clients.CUI[0]
#orderingClient.nrInreg = Clients.nrInreg[0]
#orderingClient.address = Clients.address[0]
#orderingClient.isCompany = Clients.isCompany[0]
#
#orderedProds.productName.insert(0, Products.productName[0])
#orderedProds.productPrice.insert(0, Products.productPrice[0])
#orderedProds.productQuantity.insert(0, 2)

def menu():   
    #Products = xlsx.getAllProducts()
    #Clients = xlsx.getAllClients() 

    print("------ Wellcome to Invoice Service ------")
    print("1. View all clients")
    print("2. Add a new client")
    print("3. Select a client for the invoice")
    print("4. Select an existing product for invoicing")
    print("5. Add a new pruduct to the invoice")
    print("6. Edit a slected product")
    print("0. Exit")
    
    choice = input()
    if choice == "0":
        raise SystemExit
    if choice == "1":
        print("Choice 1")
        wait = input()
        menu()
    if choice == "2": 
        print("Choice 2")
        wait = input()    
        menu()

def main():
    menu()






#Logger.Log("{}: {} {} {}".format(__name__, Products.productId[0], Products.productName[0], Products.productPrice[0]))
#InvoiceMaker.TestMe(orderedProducts)
#InvoiceMaker.MakeInvoice(orderedProducts, customerInfo, 55)
#file.getAllClients()
#file.getAllProducts()

if __name__ == "__main__":
    main()