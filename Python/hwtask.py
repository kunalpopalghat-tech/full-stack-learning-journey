# -----------------------------
# Task 1 : Identity Card
# -----------------------------

# print("========== MY ID CARD ==========")

name = "Kunal"
age = 19
city = "Sambhajinagar"
dob = 19-9-2006
college = "Vasantrao Naik Vidyalay"
blood = " - "

print("\n========== MY ID CARD ==========")
print("Name        :" ,name)
print("Age         :" ,age)
print("City        :" ,city)
print("DOB         :" , dob)
print("College     :" ,college)
print("Blood Group :" ,blood)
print("===============================")

# -----------------------------
# Task 2 : Data Types
# -----------------------------

print("\nTask 2 : Find Data Types")

a = 25
b = 2.5
c = "Twenty Five"
d = True
e = 2 + 3j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# -----------------------------
# Task 3 : Memory Detective
# -----------------------------

print("\nTask 3 : Memory Detective")

v1 = 100
v2 = 100
v3 = 100

print("v1 :", id(v1))
print("v2 :", id(v2))
print("v3 :", id(v3))

print("v1 is v2 :", v1 is v2)
print("v2 is v3 :", v2 is v3)