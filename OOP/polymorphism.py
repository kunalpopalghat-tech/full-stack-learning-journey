# # Polymorphism :
# -- defination 
# -- Types of polymorphism 

# -- overloading 
# -- overriding



# Q . What is polymorphisms ?
# ---> it is the one of the important pillars of OOP .
# ---> The same name entity behaves differently at different times ans is called polymorphisms .

# --> poly --> "many ".
# --> morphs --> "forms".

# -> There is two types of polymorphis :

# 1. overloading :
# 		1.operator overloading 
# 		2.method/constructor overloading

# 2. overriding :
# 		1.Method overriding
# 		2.Variable overriding`																										


class Book :
    def __init__(self,t,p):
        self.title = t
        self.price = p

    def __add__(self, other):
        return self.title + other.title

b1 = Book("core python",200)
b2 = Book("advanced python",600)

print(b1 + b2)