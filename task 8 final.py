#1 Create a program class called circle with constructor which will take a list as an argument for the task.
#The List is[10,501,22,37,100,999,87,351]
class Circle:
    # constructor
    def __init__(self):
        # initializing instance variable
        self.num=[10,501,22,37,100,999,87,351]

    # a method
    def read_number(self):
        print(self.num)


# creating object of the class. This invokes constructor
obj = Circle()

# calling the instance method using the object obj
obj.read_number()

OUTPUT:
[10, 501, 22, 37, 100, 999, 87, 351]

#2 Create proper member variables inside the task if required and use them when necessary.For example for this task 
# create a class private variable named pi=3.141
class myClass:
   a = 33;
   def __privMeth(self):
      print("I'm inside class myClass")
   def hello(self):
      print("Private Variable value: ",myClass.a)
foo = myClass()
foo.hello()
foo.a

OUTPUT: 
Private Variable value:  33

#3 From the given List create two class Methods Area and Perimeter which will be going to calculate the Area 
# Area and Perimeter
class Circle():
   
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**3.141
    
    def perimeter(self):
        return 2*self.radius*3.141

NewCircle = Circle(7)
print(NewCircle.area())
print(NewCircle.perimeter())

OUTPUT:
451.2871252038085
43.974000000000004


class TvClass:
    def _init_(self,brand, channel=1, price, inches, OnOFF, volume=50)
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.OnOFF = OnOFF
        self.volume = volume

    def increasevolume(self):
        if self.volume < 100:
            self.volume += 1

    def decreasevolume(self):
          if self.volume > 100:
            self.volume -= 1     

    def changechannel (self, channelnumber):
        if 0 <= channelnumber <= 50;
            self.channel = channelnumber

    def reset(self):
        self.channel = 1
        self.volume = 50

    # Panasonic at channel 8, volume 75
    def showstatus(self):
        print(f"{self.brand} at channel {self.channel},volume{self.volume}")  

Class Plasma:
     pass

Class LED:
     pass

plasma = Plasma("Panasonic", 80000, 75, "On") 
plasma.showstatus()
plasma.increasevolume()
plasma.increasevolume()
plasma.changechannel(70)
plasma.showstatus()



