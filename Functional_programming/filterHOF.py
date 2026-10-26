# filter  HOF :-
#---> filter is higher order function (HOF), because it takes a function as an argument.
#---> filter higher order function is used to filter out iterable as per given function logic .

# syntax :-

# filter(function,iterable)

# Example :- Even number code  
numbers = [1,2,3,4,5,6]

def is_even(n):
    return n % 2 == 0

res = filter(is_even , numbers)

print(list(res)) # 

# filter() filters element from an iterable based on function that returns a true or false .
# because it accepts the function as an argument , it is a higher order function .