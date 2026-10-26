# Lambda function :-
#---> A lambda function is a small anonymous function in python that can contain only a single expression and 
# is defined using the lambda keyword .

# syntsx :-
# lambda var/argument : expression

# lambda --> it is keyword used to create a lambda function.
# var/argument --> inputs to the function .
# expression --> operation whose result is returned automatically   

# Example :-
# normal function :-
def add(a,b) :
    return a+b
print(add(10,20)) # output : 30

# lambda function :-
add = lambda a , b : a + b
print(add(10,20)) # output : 30

# Both function produce a same result.

# Lambda with filter function :-

E_salary = {"rahul":45000,"priya":65000,"amit":38000,"sneha":72000,"raj":55000}

emp_dict = dict(filter(lambda s : s[1] > 50000, E_salary.items()))

print(emp_dict) # output : {'priya': 65000, 'sneha': 72000, 'raj': 55000}