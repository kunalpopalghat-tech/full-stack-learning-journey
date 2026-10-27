# Hibrid inheritance :-
#---> it is combination of two or more than two types of inheritance is hybrid inheritance .

# Example :-

class A :
    def m1(self) :
        print("m1 method of A class")

class B(A) :
    def m2(self) :
        print("m2 method of B class")

class C(A) :
    def m3(self) :
        print("m3 method of C class")

class D(A) :
    def m4(self) :
        print("m4 method of D class")

class E :
    def m5(self) :
        print("m5 method of E class")

class F(B) :
    def m6(self) :
        print("m6 method of F class")

class G(C) :
    def m7(self) :
        print("m7 method of G class")

class H(D,E) :
    def m8(self) :
        print("m8 method of H class")

obj1 = F()

obj2 = G()

obj3 = H()

obj1.m1()
obj2.m3()
obj3.m8()

print(F.mro()) #[<class '__main__.F'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
print(G.mro()) #[<class '__main__.G'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(H.mro()) #[<class '__main__.H'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.E'>, <class 'object'>]