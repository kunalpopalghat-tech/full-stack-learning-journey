# def fun1(n1) :

#     print("we are inside function 1 ")

#     def fun2(n2) :

#         print("we are inside function 2 ")

#         def fun3(n3) :
#             return n1 + n2 +n3
#             # print("we are inside function 3 ")

#         return fun3

#     return fun2

# base_100 = fun1(100)
# base_500 = base_100(300)
# base_1000 = base_500(500)
# base_1000 = base_500(600)
# base_1000 = base_500(1000)
# # base_1000 = base_500(700)

# print(base_1000)


def f1() :

    def f2() :

        def f3() :

            print("Hello world")

        return f3

    return f2



f2 = f1()
f3 = f2()
f3()
f3()
f3()
f3()
f3()