# Student class initialization
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        # Make grade private
        self.__grade = grade

    # Method to display student info
    def display_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nGrade: {self.__grade}"

    # Getter for private grade
    def get_grade(self):
        return self.__grade

    # Setter for private grade
    def set_grade(self, new_grade):
        self.__grade = new_grade


# GraduateStudent class inheriting from Student
class GraduateStudent(Student):
    def __init__(self, name, age, grade, degree):
        # Call parent constructor
        super().__init__(name, age, grade)
        self.degree = degree

    # Method overriding (Polymorphism)
    # to override the display_info
    def display_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nDegree: {self.degree}\nGrade: {self.get_grade()}"


# Create objects
student1 = Student("Destine", 19, "A")
student2 = GraduateStudent("John", 24, "B+", "MSc Computer Science")
student3 = GraduateStudent("Elder", 23, "A-", "BSc Agriculture")

# Display info
print("=========================")
print(student1.display_info())
print("=========================")
print(student2.display_info())
print("=========================")
print(student3.display_info())
print("=========================")


# Update grade for student1
student1.set_grade("A+")
print("\nUpdated Info for Student1:")
print(student1.display_info())
