# What is MRO in python ?
#--->MRO(Method resolution order) is the order in which python researches
#  for a method or attributes when a class uses inheritance

# python uses the c3 linerization algorithm to determine MRO , especially in multiple inheritance

# There is two ways to find MRO of class in python 

# 1 . mro() :- method
#---> mro() is method that returns the method resolution order .

# mro() method returns list type of data in output 

# Example :-
class A :
    def m1(self) :
        print("m1 method of class A")

class B(A) :
    def m2(self) :
        print("m2 method of class B")

obj = B()

obj.m1()

print(B.mro()) #[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

print(type(B.mro())) # <class 'list'>



# 2. __mro__ :- Atributes
#---> __mro__ is special attribute of a class that stores the Method Resolution Order of that class.

# __mro__ special attribute return tuple type of data in output 

# Example :-

class C :
    def m1(self) :
        print("m1 method of class A")

class D(C) :
    def m2(self) :
        print("m2 method of class B")

obj1  = D()
obj1.m1()
obj1.m2()

print(D.__mro__) # (<class '__main__.D'>, <class '__main__.C'>, <class 'object'>)

print(type(D.__mro__)) # <class 'tuple'>