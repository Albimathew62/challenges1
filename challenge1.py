char1=input("enter the characters:")
vowels=['a','e','i','o','u','A','E','I','O','U']
vowel=0
consonant=0

for i in char1:
    if i in vowels:
        vowel+=1
    else:
        consonant+=1
print("no of vowels:",vowel)
print("no of consonants:",consonant)






#palindrome



text=input("enter the string:")
text1=text[::-1]
if text==text1:
    print("it is palindrome")
else:
    print("it is not palindrome")



#string

# text=input("enter the string:")

# text1=("")
# for i in text:
#     if i not in text1:
#         text1+=i

# print(text1)




# task4

# num=list(map(int,input("enter the list of numbers:").split()))

# total=sum(num)
# no=len(num)
# average=total/no

# print("sum of the numbers:",total)
# print("average of the numbers:",average)


#task 5


# def fun(mylist):
#     newlist=mylist[::-1]
#     return newlist
# mylist=list(map(int, input("Enter the list of numbers:").split()))
# print("reversed list:",fun(mylist))



# #task 6
# def duplicate(mylist):
#     newlist=[]
#     for i in mylist:
#         if i not in newlist:
#             newlist.append(i)
#     return newlist
# mylist=input("Enter the characters of the list:").split()
# print("new list without duplicate elements:",duplicate(mylist))




#task 7

# list1=set(map(int,input("enter the first list of numbers:").split()))
# list2=set(map(int,input("enter the second list of numbers:").split()))

# newlist=list1.intersection(list2)
# print("new list:",(newlist))




#task 8

# def myelements(list,element):
#     num=0
#     for i in list:
#         if i==element:
#             num+=1
#     return num

# list=list(map(int,input("enter the list of numbers:").split()))
# element=int(input("enter the element to be counted:"))

# print("no of times the element appeared:",myelements(list,element))


#task9

# def count(tupl,elemnt):
#     num=0
#     for i in tupl:
#         if i==elemnt:
#             num+=1
#     return num

# tuple1=tuple(map(int,input("enter the tuple of numbers:").split()))
# element=int(input("enter the element to be counted:"))
# print("no of times the element appeared:",count(tuple1,element))



#task 10

# def avg_age(persons):
#     age=0
#     count=0
#     for j,i in persons:
#         age+=i
#         count+=1
#     avg=age/count
#     return avg

# pep_age=[('alan',23),('rahul',25),('josu',24),('albi',56)]
# avg_age(pep_age)
# print("average age:",avg_age(pep_age))

#task 11

# seta=set(map(int,input("enter the first set of numbers:").split()))
# setb=set(map(int,input("enter the second set of numbers:").split()))

# setc=seta.intersection(setb)

# print(setc)


#task12
# def unique(string):
#     str2=set()
#     for i in string:
#         if i in str2:
#             return False
#         str2.add(i)
        
#     return True
# string=input("enter the string:")
# print(unique(string))


#task13

# def highp(items):
#     maxp = max(items.values())  
#     for item, price in items.items():
#         if price == maxp:
#             print(item)  
# items = {}  
# for i in range(5):
#     item = input("Enter item name: ")  
#     price = int(input("Enter item price: "))  
#     items[item] = price 

# highp(items)


#task14
# key=["name","age","address"]
# value=["albi",21,"kerala"]

# dict={}

# for i in range(len(key)):  
#     dict[key[i]]=value[i]

# print(dict)


# #task16

# a= input("enter the number to be checked:")
# b=a[::-1]
# if a==b:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")


#task17


# a=input("enter the number:")
# tsum=sum(map(int,a))
# print("sum of the numbers:",tsum)


#task15

# def amstrong(num):
#     numst=str(num)
#     numdig=len(numst)

#     s1= sum(int(digit) ** numdig for digit in numst)
#     return s1 == num
# num2 = int(input("Enter a number: "))

# if amstrong(num2):
#     print(f"{num2} is an Armstrong number.")
# else:
#     print(f"{num2} is not an Armstrong number.")


#task18

# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")  
#         a, b = b, a + b  

# fibonacci(12)

#task19


# for i in range(1, 6):
#     print('*' * i)
# print( )



# num = 1
# for i in range(1, 5):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()
# print()


# rows = 4
# for i in range(rows):
#     print(' ' * (rows - i - 1) + '* ' * (i + 1))
# print()




# for i in range(6, 0, -1):
#     for j in range(i, 7):
#         print(j, end="")
#     print()


#task 20

# def table(num,l=10):
#     for i in range(1,10):
#         print(num, "x", i, "=", num * i)

# table(5)


#task21


# num = 5
# fact = 1

# for i in range(1, num + 1):
#     fact *= i

# print(f"The factorial of {num} is {fact}")

#task22

# num = int(input("Enter a number: "))


# for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#         print(f"{num} is not a prime number")
#         break
# else:
#     print(f"{num} is a prime number")


# task23
# num = [1, 3, 5, 7, 9] 

# for i in range(len(num)):  
#     print(" " * i, end="") 
#     for j in range(i, len(num)):  
#         print(num[j], end="")  
#     print() 


# task23
# num = "13579"

# for i in range(len(num)):  
#     print(num[i:])




#task24

# sq = [x**2 for x in range(1, 11)]
# print(sq)






#________________________________________________________


#task25
# string = input("Enter a string: ")  
# n = 1 

# for char in string:
#     print(f"Character {n}:{char}")
#     n+=1




#task26
# str=["Python","Hello","Java"]
# upp=[]

# for word in str:
#     for char in word:
#         if char.isupper():
#             upp.append(char)

# print(upp)





#task27


# num=[10,4,3,32,11,5,8,20,2,15,7,30]


# num.sort()

# sec= num[1]
# third= num[-3]
# print(f"Second Smallest:{sec}")
# print(f"Third Largest:{third}")







#task28


# num1=[1, 2, 3, 4, 2, 3, 5, 6, 1, 7]
# uniq=[]
# for num in num1:
#     if num not in uniq:
#         uniq.append(num)

# print(uniq)



#task29

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     return x / y


# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = input("Enter choice: ")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if choice == '1':
#     print(f"Result: {add(num1, num2)}")
# elif choice == '2':
#     print(f"Result: {subtract(num1, num2)}")
# elif choice == '3':
#     print(f"Result: {multiply(num1, num2)}")
# elif choice == '4':
#     print(f"Result: {divide(num1, num2)}")
# else:
#     print("Invalid input")



#task30

# def count(string):
#     vowels = "AEIOUaeiou"
#     vc= 0
#     cc= 0

#     for char in string:
#         if char.isalpha(): 
#             if char in vowels:
#                 vc+=1
#             else:
#                 cc+= 1

#     print("Vowels:", vc)
#     print("Consonants:", cc)


# str=input("Enter a string: ")
# count(str)


#task31


# class Product:
#     def __init__(self, name, price, quantity=1):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#     def update_quantity(self, quantity):
#         self.quantity += quantity

#     def get_total_price(self):
#         return self.price * self.quantity

# class ShoppingCart:
#     def __init__(self):
#         self.cart = {}
    
#     def add_product(self, product):
#         if product.name in self.cart:
#             self.cart[product.name].update_quantity(product.quantity)
#         else:
#             self.cart[product.name] = product
    
#     def remove_product(self, product_name):
#         if product_name in self.cart:
#             del self.cart[product_name]
#         else:
#             print(f"{product_name} not found in the cart.")
    
#     def calculate_total(self):
#         return sum(product.get_total_price() for product in self.cart.values())
    
#     def display_cart(self):
#         if not self.cart:
#             print("Your cart is empty.")
#             return
#         print("Shopping Cart:")
#         for product in self.cart.values():
#             print(f"{product.name} - {product.price} x {product.quantity} = {product.get_total_price()}")
#         print(f"Total Price: {self.calculate_total()}")

# cart = ShoppingCart()

# cart.add_product(Product("Laptop", 55000, 1))
# cart.add_product(Product("Mouse", 500, 2))
# cart.add_product(Product("Keyboard", 800, 1))
# cart.add_product(Product("Mouse", 500, 1)) 

# cart.display_cart()

# cart.remove_product("Keyboard")

# cart.display_cart()




# def tri(n):
#     for i in range(n):
#         num=1
#         print(""*(n-i),end="")
#         for j in range(i+1):
#             print(num,end="")
#             num=num*(i-j)//(j+1)
#         print()


# tri(5)


num=1
row=5
for i in range(1,row+1):
    for j in range(1,i+1):
        print(num,end="")
        num+=1
    print()
              