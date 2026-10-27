# Hierarchical inheritance :-
#---> one parent class and multiple child classes that kind of inheritance is called as hierarchical inheritance .

# in hierarchical inheritance all child class can access property of one parent class .

# Example :-

class Parent :

    def m1(self) :

        print("we are inside m1 of parent class")

class child1(Parent) :

    def m2(self) :

        print("we are inside m2 of child1 class")

class child2(Parent) :

    def m3(self) :

        print("we are inside m3 of child2 class")

class child3(Parent) :

    def m4(self) :

        print("we are inside m4 of child3 class")

a = child1()
b = child2()
c = child3()

a.m1()
b.m1()
c.m1()

print(child1.mro()) #[<class '__main__.child1'>, <class '__main__.Parent'>, <class 'object'>]

print(child2.mro()) #[<class '__main__.child2'>, <class '__main__.Parent'>, <class 'object'>]

print(child3.mro()) #[<class '__main__.child3'>, <class '__main__.Parent'>, <class 'object'>]

