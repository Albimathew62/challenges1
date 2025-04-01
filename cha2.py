# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class ShoppingCart:
#     def __init__(self):
#         self.cart = {}

#     def add_product(self, product, quantity):
#         if product.name in self.cart:
#             self.cart[product.name]['quantity'] += quantity
#         else:
#             self.cart[product.name] = {'product': product, 'quantity': quantity}

#     def remove_product(self, product_name):
#         if product_name in self.cart:
#             del self.cart[product_name]

#     def calculate_total(self):
#         total = sum(item['product'].price * item['quantity'] for item in self.cart.values())
#         return total

#     def show_cart(self):
#         for item in self.cart.values():
#             print(f"{item['product'].name} - {item['quantity']} x {item['product'].price}")


# p1 = Product("Laptop", 50000)
# p2 = Product("Phone", 20000)

# cart = ShoppingCart()
# cart.add_product(p1, 1)
# cart.add_product(p2, 2)
# cart.show_cart()
# print("Total:", cart.calculate_total())

# cart.remove_product("Phone")
# cart.show_cart()
# print("Total after removing phone:", cart.calculate_total())





#32


# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def getBookInfo(self):
#         return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# book1 = Book("harry potter","J.K.Rowling", 1990, )
# print(book1.getBookInfo())

# book2 = Book("mahabarat", "vyas", 1900)
# print(book2.getBookInfo())


#33

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def calculateArea(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculateArea(self):
#         return 3.14 * self.radius * self.radius 

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculateArea(self):
#         return self.length * self.width


# c = Circle(5)
# r = Rectangle(4, 6)

# print("Circle Area:", c.calculateArea())
# print("Rectangle Area:", r.calculateArea())



#34

# class MathUtils:
#     @staticmethod
#     def calculateSum(num):
#         return sum(num)


# num = [1, 2, 3, 4, 5]
# result = MathUtils.calculateSum(num)
# print(f"Sum of numbers: {result}")  


#35

# from abc import ABC, abstractmethod

# class PaymentMethod(ABC):
#     @abstractmethod
#     def processPayment(self, amount):
#         pass

# # class CreditCardPayment(PaymentMethod):
# #     def processPayment(self, amount):
# #         print(f"Processing gpay payment of {amount}rs...")

# # class PayPalPayment(PaymentMethod):
# #     def processPayment(self, amount):
# #         print(f"Processing Paytm payment of {amount}rs...")

# # def make_payment(payment_method, amount):
# #     payment_method.processPayment(amount)

# # credit_card = CreditCardPayment()
# # paypal = PayPalPayment()

# # make_payment(credit_card, 100)
# # make_payment(paypal, 50)



# #36

# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Lion(Animal):
#     def sound(self):
#         return "roars"

# class Tiger(Animal):
#     def sound(self):
#         return "growls"

# lion = Lion()
# tiger = Tiger()

# print(lion.sound())
# print(tiger.sound())









#37

# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod

#     def calcArea(self):
#         pass
#     def calcPeri(self):
#         pass

# class circel(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def calcArea(self):
#         return math.pi*self.radius*self.radius
#     def calcPeri(self):
#         return 2*math.pi*self.radius
    
# class rectangle(Shape):
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def calcArea(self):
#         return self.length*self.width
#     def calcPeri(self):
#         return 2*(self.length+self.width)

# circle=circel(5)
# rectangle=rectangle(4,6)

# print(f"Circle Area: {circle.calcArea():}")
# print(f"Circle Perimeter: {circle.calcPeri():}")

# print(f"Rectangle Area: {rectangle.calcArea():}")
# print(f"Rectangle Perimeter: {rectangle.calcPeri():}")


#38
# alpha = iter("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# while True:
#     try:
#         print(next(alpha), end=" ")

#     except StopIteration:
#         break



#39


# def half(start=1,end=10,inter=0.5):
#     while start<=end:
#         yield start
#         start+=inter

# for num in half():
#     print(num,end=" ")





# class iter:
#     def __init__(self,start=1,end=10,inter=0.5):
#         self.start=start
#         self.end=end
#         self.inter=inter

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         value = self.current
#         self.current += self.step
#         return value

# half=iter()   

# for num in half:
#     print(num, end=" ")

#40


# sub = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# newlist = sorted(sub, key=lambda x: x[1])
# print(newlist)

#41



# phones = [
#     {'make': 'Nokia', 'model': 216, 'color': 'Black'},
#     {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
# ]


# sort1=sorted(phones, key=lambda x:(x['model']))

# print(sort1)


#42


# num= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squares = list(map(lambda x: x**2, num))
# cubes = list(map(lambda x: x**3, num))

# print("Squares are:", squares)
# print("Cubes are:", cubes)



# num= [1,2,3,4,12,13,19,26,38,40,41,42,43]
# resu=list(filter(lambda x:x%13==0 or x%19==0,num))
# print(resu)


#45

# num=[1,2,3,4,5,10,-1,-2,-3,-4,-5]

# pos=list(filter(lambda x:x>0,num))
# neg=list(filter(lambda x:x<0,num))

# pos_sum=sum(pos)
# neg_sum=sum(neg)

# print("sum of positive no",pos_sum)
# print("sum of negative no",neg_sum)


#46

# def countT():
#     n=0
#     with open("story.txt","r") as file:
#         for line in file:
#             if not line.startswith("T"):
#                 n+=1
#     print(n)

# countT()

#47

# def count():
#     n=0
#     with open("story.txt","r") as file:
#         for line in file:
#             line=line.strip()
#             if line[-1]=="e":
#              n+=1
#     print(n)

# count()

#48
# def count():
#     n=0
#     file= open("story.txt","r")
#     for line in file:
#             for word in line.split():
#                n+=1
#     file.close()
#     print(n)

# count()

#49

# import re

# def is_valid(s):
#     pattern ='^[a-zA-Z0-9]+$'
#     return bool(re.match(pattern, s))

# test=input("Enter a string:")
# if is_valid(test):
#     print("valid")
# else:
#     print("invalid")



#50
import  re 
def is_valid(s):
    pattern='^a[b]$'
    return bool(re.match(pattern,s))

test=input("Enter a string:")
if is_valid(test):
    print("valid")
else:
    print("invalid")



