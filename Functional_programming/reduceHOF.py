# Redece HOF :-
#---> Reduce is higher order function (HOF), because it takes function as an argument.
#-> It is available in functools module .

# syntax :-
# from functools import reduce 
# reduce (function , iterable)

# Example :- sum of numbers 

from functools import reduce

numbers = [1,2,3,4,5,6]

def add(a,b) :
    return a+b

res = reduce(add , numbers)
print(res)


# Reduce is higher order function that repeatedly applies a function to the element of an iterable 
# and reduces them to a single final value 