# product_list = [1200,900,1500,850,350,2400]

# def costlier_products(motu_list):
#     chotu_list = []
#     for price in motu_list :
#         if price > 1000 :
#             chotu_list.append(price)
#     return(chotu_list)

# cost_product_list = costlier_products(product_list)
# print(f"The costlier products are : {cost_product_list}")


# def total_bill(products):
#     total = 0
#     for price in products:
#         total += price
#     return total

# product_list = [1200,900,1500,850,350,2400]

# total_amount = total_bill(product_list)

# print(f"The total bill amount is : {total_amount}")



# def frequency_character(s) :
#     s_dict = {}
#     for ch in s:
#         if ch in s_dict.keys():
#             s_dict[ch] = +1
#         else :
#             s_dict[ch] = 1
    
#     return s_dict


# s = "Instagram"

# freq_dict = frequency_character (s)
# print(f"frequency of each character in this string is :{freq_dict}")


# Nested function in python  
#-----> A nested function inside that is defined inside another function 
#-----> In simple words : function inside function = Nested function 

# Example 

# def outer_fun() :
#     print("we are inside outer function ")

#     def inner_fun() :
#         print("we are inside inner function ")


#     inner_fun()


# outer_fun()



#  clousers in pytthon :

# Example :

def add(n1):

    def addTwo(n2):
        return n1+n2

    return addTwo


base_100 = add(100)

print(base_100(40))
print(base_100(140))
print(base_100(50))
print(base_100(80))

base_500 = add(500)

print(base_500(40))
print(base_500(200))
print(base_500(70))
print(base_500(100))

base_1000 = add(1000)

print(base_1000(90))
print(base_1000(900))
