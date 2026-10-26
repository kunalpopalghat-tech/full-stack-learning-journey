# student has age and location . student has operations like studying and playing 

class student :
    def __init__(self, a, l):
        self.age = a
        self.location = l

    def study(self):
        print("python")

    def playing(self):
        print("cricket")


s1 = student(20,"pune")
print(s1.age)
print(s1.location)