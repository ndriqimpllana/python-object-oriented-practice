# Class Definition
class Student:
    def __init__(self, name, email, grades=None):
        self.name = name
        self.email = email
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade():.2f}")
        print("-" * 40) #add a line just to separate each student for better readability

    #Return grades as a tuple
    def grades_tuple(self):
        return tuple(self.grades)


s1 = Student("Ndricim Pllana", "ndricim@example.com", [85, 78])
s2 = Student("Donat Pllana", "donat@example.com", [88, 80])
s3 = Student("Yigit Senyanyla", "yigit@example.com", [83, 89])

# Add two grades to each student
for student in (s1, s2, s3):
    student.add_grade(95)
    student.add_grade(87)

# Display each student's info and average
print("\n--- STUDENT INFORMATION ---\n")
for student in (s1, s2, s3):
    student.display_info()



#Dictionary & Set Integration


student_dict = {
    s1.email: s1,
    s2.email: s2,
    s3.email: s3
}

def get_student_by_email(email):

    #Retrieve a student by email using dictionary with the  .get() method.

    student = student_dict.get(email)
    if student:
        print(f"Found student: {student.name}")
        return student
    else:
        print(f"No student found with email: {email}")
        return None


# Tuple Practice


print("\n--- GRADES AS TUPLES ---\n")
for student in (s1, s2, s3):
    grades_tuple = student.grades_tuple()
    print(f"{student.name}'s Grades Tuple: {grades_tuple}")


    
    # Demonstrate immutability
    try:
        grades_tuple[0] = 100  # Attempt to modify tuple (should raise TypeError)
    except TypeError:
        print(f"Tuples are immutable! Cannot modify {student.name}'s grades.\n")



# List Operations


print("\n--- LIST OPERATIONS ---\n")
for student in (s1, s2, s3):

    # Remove the last grade

    removed = student.grades.pop()
    print(f"Removed last grade ({removed}) from {student.name}")

    # Access first and last grade

    first_grade = student.grades[0]
    last_grade = student.grades[-1]
    print(f"{student.name}'s first grade: {first_grade}, last grade: {last_grade}")

    # Print number of grades

    print(f"{student.name} now has {len(student.grades)} grades.\n")

print("--- END OF PROGRAM ---")
