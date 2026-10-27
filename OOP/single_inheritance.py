# Single / simple inheritance :-
#---> one parent and one child class kind of inheritance is called  single / simple inheritance.

# only child class can access the property of parent class .

# Example :-

class A : # parent class  

    def m1(self,a,b) :

        print(f"addition is :{a+b}")

class B(A) : # child class 

    def m2(self,a,b) :

        print(f"subtraction is :{a-b}")




obj1 = B()
obj1.m1(10,20)
obj1.m2(10,20)

print(B.mro()) # [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>] this the MRO of class B.