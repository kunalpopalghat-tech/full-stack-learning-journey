# create a HOF which accepts one function and one list as an arguments . 
# your HOF should be return all even numbers from given list .
# # MY solution :
# num_list = [1,2,3,4,5,6,7,8,9]


# def f1(numbers) :
#     for i in num_list :
#         if i % 2 == 0 :
#             print("Even numbers is --------->", i)

# # f1(num_list)

# def my_hof(f,l) :
#     f(num_list)
#     print("numbers list is :",l)


# my_hof(f1,num_list)


#Atul sir's solution :


def f1(num) :

    return num % 2 == 0

    # if num % 2 == 0 :
    #     return True
    # else :
    #     return False

def f2(num) :

    return num % 2 != 0


def my_hof(f2,l) :
    odd_list = []
    for i in l :
        if f2(i):
            odd_list.append(i)
            # print(even_list)
    print("This is even list :",odd_list)
    return odd_list

lst = [1,2,3,4,5,6,7,8,9]

# even_list = my_hof(f1,lst)

odd_list = my_hof(f2,lst)