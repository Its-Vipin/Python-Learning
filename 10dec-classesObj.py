# # class Laptop:
# #     def config(self):
# #         print("Acer","i5-1240P","RTX 2050","8GB","512GB")

# # laptop1 = Laptop
# # laptop1.config(laptop1)


# # # -------------------------------------------------------------
# # class Laptop:
    
# #     def config():
# #         print("Acer","i5-1240P","RTX 2050","8GB","512GB")

# # laptop1 = Laptop
# # laptop1.config()


# # ------------------------------------------------------------------
# class Laptop:
#     def __init__(self):
#         print("Hello WOrld")
#     def config(self):
#         print("Acer","i5-1240P","RTX 2050","8GB","512GB")

# laptop1 = Laptop()
# laptop1.config()


# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno

#     def info(self):
#         print("Name is:",self.name, self.rollno)
# s1=student("Vipin",71)
# s1.info()              
# print(id(s1))


# class Person:
#     def __init__(self):
#         self.name="Ishan"
#         self.no=32

#     def compare(self,other):
#         if (self.no==other.no):
#             return True
#         else:
#             return False       

# p1=Person()
# p2=Person()
# p2.no=18 
# if p1.compare(p2):
#     print("same")
# else:
#     print("different")    
    



class car:
    wheel=4
    # Static variable - 
    # Instance variables - values varies from object to object.
    def __init__(self):
        self.company="BMW"
        self.mileage=10
        
car1=car()
car2=car()

car1.wheel=5
print(car1.mileage)
print(car2.mileage)

print(car1.wheel)
print(car2.wheel)
