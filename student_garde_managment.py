#Inicilaizing Students
student_grades={ }

#Add a new Student
def add_student(name,grade):
    student_grades[name]=grade
    print(f"The Student name is '{name}' and his grade is '{grade}'")

#Update Student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"Update Sussces")
        option=input("Enter 1 if you see grade")
        if option==1:
            print(f"The Student name is '{name}' and his grade is '{grade}'")
    else:
        print(f"Student {name} is not Found in database") 

#deleteG Student
def delet_student(name):
    if name in student_grades:
        del student_grades[name]
        print("Student name delet sucssesfuly")
    else:
        print(f"{name} is not found in database")

#view all Student
def veiw_all():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
        
#main funtion
def main():
    while True:
        chose=input("""
                    1. Add Student
                    2. Update Student
                    3. Delet Student
                    4. View All Student
                    5. Exit""")
        if chose=="1":
            name=input("Enter the Student name ")
            grade=int(input("Entre the Studetn Grade "))
            add_student(name, grade)
        elif chose=="2":
            name=input("Enter the Student name ")
            grade=int(input("Entre the Studetn Grade "))
            update_student(name, grade)
        elif chose=="3":
            name=input("Enter the Student name ")
            delet_student(name)
        elif chose=="4":
            veiw_all()
        elif chose=="5":
            print("Goodbuy")
            break
        else:
            print("invalid Chose")
if __name__=='__main__':
    main()