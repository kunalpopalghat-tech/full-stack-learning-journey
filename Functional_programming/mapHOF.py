# inbuild higher order function :

# 1.Map :-
#---> Map function will accept another function and one iterable (List ,tuple ,string ,dictionary)
# and returns map object as per the function logic .

#-> It is basically used for map data .

# Example :-

def add_five(m) :
    if m < 90 :
        return m+5
    else :
        return m

marks = [67,87,91,99,87,65,45]

res = list(map(add_five,marks))
print(marks)
print(res)