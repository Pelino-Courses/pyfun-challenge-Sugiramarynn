
Inventory = {}
class product:
    def __init__(self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.Product= {}
    def add_product(self):
        product_add = str(input("Enter Product Name:"))
        price_add = int(input("Enter Product Price:"))
        Quantity_add = int(input("Enter Product Quantity:"))
        self.Product["Name"]= product_add
        self.Product["Price"]= price_add
        self.Product["Quantity"]= Quantity_add
        key = len(Inventory)+1
        Inventory[key]= self.Product
        return Inventory
    def remove_product(self):
        product_id = int(input("Enter Product ID:"))
        for x in Inventory.keys():
            if product_id in Inventory:
                del Inventory [product_id]
                return f"The remained product is:{Inventory}"
            else:
                return"Invalid Product ID"
            
    def total_value(self):
        product_id = int(input("Enter Product ID:"))
        for x in Inventory.keys():
            if product_id in x:
                total = self.Product["price"]*self.Product["Quantity"]
                return f"The total price of the:{self.Product["Name"]} is :{total}"
            else:
                print("Invalid product ID")
counter=0
while(True):
    def main():
        print("product Details:\n1.Add Product\n2.Product Remove\n3.Calculate total price")
        choice=int(input("Enter Your choice :"))
        if choice==1:
            A=product("",0,0)
            print(A.add_product())
        elif choice==2:
            A=product("",0,0)
            print(A.remove_product())
        elif choice==3:
            A=product("",0,0)
            print(A.total_value())
        else:
            print("Invalid Option")
    if __name__=="__main__":
        main()
    counter +1    


     

    



        

        
        