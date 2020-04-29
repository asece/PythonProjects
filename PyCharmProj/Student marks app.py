#  Last sanity check: 2020-04-29
student_list = []

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def average_mark(self):
        number = len(self.marks)
        if number == 0:
            return 0

        total = sum(self.marks)
        return total / number


def create_student():
    name = input("Please enter the new student's name: ")
    student_data = Student(name)
    return student_data

def add_mark(student, mark):
    student.marks.append(mark)


def print_student_details(student):
    print("{}, average mark: {}.".format(student.name ,
                                         student.average_mark()))

def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(student)

def add_marks(student):
    print("Add marks for student {}: ".format(student['name']))
    i = 1
    o = 1
    while (i):
        mark = input("Mark {}:".format(o))
        add_mark(student, mark)
        print("Do you want to add more marks for student {}: ".format(student['name']))
        i = int(input("0 - NO  1 - YES "))
        o += 1
        for x in range(0,4):
            print(" ")

def menu():
    sel = input("Enter  \t'p' to print the student list,\n"
                "\t\t's' to add a new student,\n"
                "\t\t'a' to add a mark for a student\n"
                " \t or 'q' to quit\n"
                "Enter selection: ")
    while sel != 'q':
        if sel == 'p':
            print_student_list(student_list)
        elif sel == 's':
            student_list.append(create_student())
        elif sel == 'a':
            student_id = int(input("Enter the student ID: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the mark: "))
            add_mark(student, new_mark)
        sel = input("Enter  \t'p' to print the student list,\n"
                    "\t\t's' to add a new student,\n"
                    "\t\t'a' to add a mark for a student\n"
                    " \t or 'q' to quit\n"
                    "Enter selection: ")


#print(s1)
#print("Student has the average: {}".format(calculate_average_mark(s1)))

menu()