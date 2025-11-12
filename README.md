# 🧑‍🎓 Object Oriented Python (OOP) Practice Assignement

## 📘 Overview
This project demonstrates my understanding of **object-oriented programming (OOP)** in Python.  
It covers the use of **classes, objects, methods, lists, dictionaries, sets, and tuples**, all structured around a single `Student` class.  
Each part builds on the previous one to show how these concepts work together in a complete program.

---

## 🧩 Features

### **Part 1: Class Definition**

I created a `Student` class with the following attributes:
- `name` (string)
- `email` (string)
- `grades` (list of integers)

The class also includes these methods:
- `add_grade(grade)` → adds a new grade to the list  
- `average_grade()` → calculates and returns the average grade  
- `display_info()` → prints the student’s details and their grades  
- `grades_tuple()` → returns the grades as a tuple  

---

### **Part 2: Working with Objects**

I created three student objects with different names, emails, and initial grades.  
Then I added new grades for each student and displayed all of their information, including their average grades.

---

### **Part 3: Dictionary & Set Integration**

I used a dictionary to map each student’s email to their corresponding `Student` object.  
Then I wrote a `get_student_by_email(email)` function to safely retrieve a student using `.get()`.  

---

### **Part 4: Tuple Practice**

I added a method that converts each student’s grades into a tuple.  
I then demonstrated that tuples are immutable by attempting to modify one inside a `try/except` block and printing an error message when it failed.

---

### **Part 5: List Operations**

Finally, I worked with lists by:
- Removing the last grade from each student’s grade list using `.pop()`
- Printing the first and last grade for each student
- Printing the total number of grades each student has using `len()`

---

## 🛠️ Technologies Used
- **Python 3.x**

---

## 🚀 How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/ndriqimpllana/python-object-oriented-practice
   cd python-object-oriented-practice
