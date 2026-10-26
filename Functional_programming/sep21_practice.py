
# def filter_student(m) :
#     return m >= 50 

# marks = [45,78,32,90,66,25,88,51,39,72]

# res = list(filter(filter_student,marks))
# print(f"all student marks {marks}")
# print(f"student who scored more than 50 marks :{res}")

E_salary = {"rahul":45000,"priya":5000,"amit":38000,"sneha":72000,"raj":55000}

def filter_salary(s) :
    return s[1] > 50000

emp_dict = dict(filter(filter_salary, E_salary.items()))

print(emp_dict)