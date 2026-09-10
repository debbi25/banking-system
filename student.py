class Student:
    def __init__(self, roll_no, name, age, department, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.department = department
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("\nRoll No:", self.roll_no)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Marks:", self.marks)
        print("Average:", round(self.average(), 2))
        print("Grade:", self.grade())


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        roll = int(input("Enter roll number: "))

        for student in self.students:
            if student.roll_no == roll:
                print("Roll number already exists")
                return

        name = input("Enter name: ")
        age = int(input("Enter age: "))
        department = input("Enter department: ")

        marks = []

        for i in range(3):
            mark = float(input("Enter mark for subject " + str(i + 1) + ": "))
            marks.append(mark)

        student = Student(roll, name, age, department, marks)
        self.students.append(student)

        print("Student added successfully")

    def display_students(self):
        if len(self.students) == 0:
            print("No students available")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        roll = int(input("Enter roll number: "))

        for student in self.students:
            if student.roll_no == roll:
                student.display()
                return

        print("Student not found")

    def delete_student(self):
        roll = int(input("Enter roll number: "))

        for student in self.students:
            if student.roll_no == roll:
                self.students.remove(student)
                print("Student deleted")
                return

        print("Student not found")


obj = StudentManagement()

while True:
    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        obj.add_student()

    elif choice == "2":
        obj.display_students()

    elif choice == "3":
        obj.search_student()

    elif choice == "4":
        obj.delete_student()

    elif choice == "5":
        print("Program ended")
        break

    else:
        print("Invalid choice")