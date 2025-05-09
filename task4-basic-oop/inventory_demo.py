from product import Product
counter=0
while(True):
    def main():
        print("product Details:\n1.Add Product\n2.Product Remove\n3.Calculate total price")
        choice=int(input("Enter Your choice :"))
        if choice==1:
            A=Product("",0,0)
            print(A.add_product())
        elif choice==2:
            A=Product("",0,0)
            print(A.remove_product())
        elif choice==3:
            A=Product("",0,0)
            print(A.total_value())
        else:
            print("Invalid Option")
        if __name__=="__main__":
            main()
    counter +1


