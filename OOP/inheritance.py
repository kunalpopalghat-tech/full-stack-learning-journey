# What is inheritance in python ?
#--> Inheritance is an one of the iportant pillars of OOP .
#--> Aquring all the properties of base class into derived class is callled inheritance .
#--> Base class is also known as super class / parent class .
#--> The derived class is also known as sub class / child class .
#--> By using inheritance we can save memory .
#--> Code redundancy is less .
#--> Debugging and testing is easy .
#--> Time required to complete project is less .
#--> We can achieve method overriding (polymorphism) by inheritance .

# There is few types of inheritance :-
#                                    1.Simple / single inheritance.
#                                    2.Multi level inheritance.
#                                    3.Multiple inheritance.
#                                    4.Hierarchical inheritance.
#                                    5.Hybrid inheritance.
#                                    6.Cyclicgvd inheritance.

class A:
    x = 10

    def m1(self):
        # print("this is method m1 of class A")
        a = 10
        return a
    
    def m2(self):
        # print("this is method m2 of class A")
        s = "instagram"
        return s


class B(A):
    y = 10

    def m3(self):
        # print("this is method m3 of class B")
        l = []
        l.append(10)
        return l
    
    def m4(self):
        # print("this is method m2 of class B")
        d = {10:"sandesh"}
        return d


obj1 = B()
obj1.m1()
obj1.m2()
obj1.m3()
obj1.m4()
print(obj1.m1())
print(obj1.m2())
print(obj1.m3())
print(obj1.m4())