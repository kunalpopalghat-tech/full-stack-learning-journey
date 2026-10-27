# multi - level inheritance :-
#---> inheritance in level is called multi - level inheritance .

# in multi-level inheritance child can access property of grand parent and parent . 

# Example :-

class Grand_parent :

    def m1(self) :
        print("We are inside method m1 of Grand_parent class")
        print("---"*30)

class Parent(Grand_parent) :

    def m2(self) :
        print("We are inside method m2 of parent class")
        print("---"*30)
        

class Child(Parent) :

    def m3(self) :
        print("We are inside method m3 of child class")
        print("---"*30)
        

obj1 = Child()

obj1.m1()
obj1.m2()
obj1.m3()

print(Child.mro())
# [<class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.Grand_parent'>, <class 'object'>] 
#  this is the MRO of class child .