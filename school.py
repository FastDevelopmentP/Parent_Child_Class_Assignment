# school.py

# Define the Person class (Parent class)
 
class Person:
    # Constructor method to initialize the Person object with name, age, and country
    def __init__(self, name: str, age: int, country: str):
        self.name = name            # Assign the provided name to the instance variable
        self.age = age              # Assign the provided age to the instance variable
        self.country = country      # Assign the provided country to the instance variable

    # Method to return a string representation of the Person object
    def __str__(self) -> str:
        # Must RETURN (not print) in this exact format
        return f"{self.name} is {self.age} years old and is from {self.country}."

    # Method to introduce the person (explicit requirement of the assignment)
    def introduce_yourself(self) -> str:
        # Returns the same information as __str__, but as a named method
        return f"{self.name} is {self.age} years old and is from {self.country}."




# Define the Student class (Child class of Person)
class Student(Person):
    # Constructor method to initialize the Student object with inherited and new attributes
    def __init__(self, name: str, age: int, country: str, major: str, gpa: float):
        # Call the constructor of the parent Person class
        super().__init__(name, age, country)
        # Set the Student-specific attributes
        self.major = major
        self.gpa = gpa

    # Method to return a string describing the student's study details
    def study(self) -> str:
        # Must return exactly this format per assignment instructions
        return f"{self.name} is studying {self.major} with a current GPA of {self.gpa}."


# Define the Staff class (Child class of Person)
class Staff(Person):
    # Constructor method to initialize the Staff object with inherited and new attributes
    def __init__(self, name: str, age: int, country: str, position: str, department: str):
        # Call the constructor of the parent Person class
        super().__init__(name, age, country)
        # Set the Staff-specific attributes
        self.position = position
        self.department = department

    # Method to return a string describing the staff member's work details
    def work(self) -> str:
        # Must return exactly this format per assignment instructions
        return f"{self.name} works as a {self.position} in the {self.department} department."


# Example usage of the classes (only runs if this file is executed directly, not when imported)
if __name__ == "__main__":
    # Step 10: Create example Person, Student, and Staff objects
    person_1 = Person("Manny", 33, "USA")                     # Example Person object
    student_1 = Student("Tammy", 19, "Vietnam", "Computer Science", 3.54)  # Example Student object
    staff_1 = Staff("Brittney", 36, "Canada", "Neuroscientist", "Biology") # Example Staff object

    # Step 11: Print outputs to demonstrate required methods
    print(person_1)                # Expected: "Manny is 33 years old and is from USA."
    print(student_1.study())       # Expected: "Tammy is studying Computer Science with a current GPA of 3.54."
    print(staff_1.work())          # Expected: "Brittney works as a Neuroscientist in the Biology department."
