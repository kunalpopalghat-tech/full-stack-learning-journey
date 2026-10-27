class Student :

    def __init__(self, n , r ,c):

        self.name = n
        self.roll_no = r
        self.course = c

    def display_student(self) :
        print(f"name :{self.name}")
        print(f"Roll number :{self.roll_no}")
        print(f"course :{self.course}")
        print("---"*30)


s1 = Student("kunal", 101 , "python full stack")
s2 = Student("sandesh", 102 , "python full stack")
s3 = Student("sagar", 103 , "python full stack")
s4 = Student("omkar", 104 , "python full stack")
s5 = Student("samadhan", 105 , " java developer ")


s1.display_student()
s2.display_student()
s3.display_student()
s4.display_student()
s5.display_student()

Student_list = [s1 , s2 , s3 , s4 , s5]

for student in Student_list :
    if "python" in student.course :
        print(f"name of student learning python:{student.name}")
        print("---"*30)

