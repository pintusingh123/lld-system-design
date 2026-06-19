class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")


class Department:
    def __init__(self, dept_name, students):
        self.dept_name = dept_name
        self.students = students  # Aggregation

    def show_students(self):
        print(f"\nDepartment: {self.dept_name}")
        print("Students List:")

        for student in self.students:
            student.display()
            print("-" * 20)


# Student objects created independently
s1 = Student("Pintu", 101)
s2 = Student("Rahul", 102)
s3 = Student("Amit", 103)

# Department uses existing Student objects
cse_dept = Department("Computer Science", [s1, s2, s3])

cse_dept.show_students()