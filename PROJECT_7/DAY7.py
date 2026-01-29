class Student :
    def __init__(self,name,roll,marks) :
        self.name=name
        self.roll=roll
        self.marks=marks

class REGISTER :
    def __init__(self,student):
        self.student=student

    def display_info(self) :
        print("---STUDENT PROFILE---")
        print(f"Name    : {self.student.name}")
        print(f"Roll_no : {self.student.roll}")
        print(f"Marks   : {self.student.marks}\n")

    def check_result(self) :
        if(self.student.marks>=40) : print("RESULT : PASS ")
        else : print("RESULT : FAIL")

NAME=input("Enter Student Name: ").strip().title()
ROLL=int(input("Enter Roll no.: "))
MARKS=int(input("Enter Marks  : "))
student=Student(NAME,ROLL,MARKS)
student_info=REGISTER(student)
student_info.display_info()
student_info.check_result()