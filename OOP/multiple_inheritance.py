# Multiple inheritance :-
#---> multiple parent classes and one child class kind of inheritance is called multiple inheritance .

# in multiiple inheritance child class can access property of both parent classes .

# Example :-

class Parent1 :

    def m1(self) :
        print("m1 is method of class parent1")

class Parent2 :

    def m2(self) :
        print("m2 is method of class parent2")

class child(Parent1,Parent2) :

    def m3(self) :
        print("m3 is method of class child")


obj = child()

obj.m1()
obj.m3()
obj.m3()


print(child.mro())
# [<class '__main__.child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>]
# this is the MRO of child class 