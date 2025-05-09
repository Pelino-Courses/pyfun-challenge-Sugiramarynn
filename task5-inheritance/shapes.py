import math
class Shape :
    def __init__(self,side):
        self.shape = side
        pass
class Circle(Shape):
    def __init__(self, side):
        super().__init__(side)
    def shape_of_figure(self):
        self.shape = 0
        return "This a circular shape"
    def shape_perimeter(self):
        self.radius = int(input("Enter the radius of the circle:"))
        self.p = math.pi
        perimeter = 2*self.p*self.radius
        return f"tHE PERIMETER OF CIRCLE IS : {perimeter}"
    def shape_area(self):
        area = self.p*self.radius**2
        return f"The area of the circle is : {area}"
class Triangle(Shape):
    def __init__(self, side):
        super().__init__(side)
    def shape_of_figure(self):
            self.shape = 3
            return f"This is a {self.shape} sided figure"
    def shape_perimeter(self):
     self.base = int(input("Enter the base of the Triangle:"))
     self.height = int(input("Enter the Height of the Triangle:"))
     self.hypotenus = int(input("Enter the Hypotenus of the Triangle:"))
     perimeter = self.base + self.height + self.hypotenus
     return f"The Perimeter of the Triangle is : {perimeter}"
    def shape_area(self):
     area = (self.base*self.height)/2
     return f"The area of the Triangle is : {area}\n"
class Rectangle(Shape):
    def __init__(self, side):
        super().__init__(side)
    def shape_of_figure(self):
        self.shape = 4
        return f"This is a {self.shape} sided figure"
    def shape_perimeter(self):
        self.length = int(input("Enter the Length of your Rectangle:"))
        self.width = int(input("Enter the Width of your Rectangle :"))
        perimeter = self.length + self.width 
        return f"The Perimeter of the Rectangle is : {perimeter}"
    def shape_area(self):
        area = self.length*self.width  
        return f"The area of this Rectangle is :{area}"    
    
def main():
    print ("Figures:\n1.Circle\n2.Triangle\n3.Rectangle")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        a= Circle(0)
        print(a.shape_of_figure(),a.shape_perimeter(),a.shape_area())
    elif choice ==2:
        t = Triangle(0)
        print(t.shape_of_figure(),t.shape_perimeter(),t.shape_area())
    elif choice ==3 :
        r =Rectangle(0)
        print(r.shape_of_figure(),r.shape_perimeter(),r.shape_area())
    else:
        print("Invalid Options")
if __name__ == "__main__":
    main()
        

