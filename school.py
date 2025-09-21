class Person:
    # Constructor method to initialize the Person object with name, age, and country
    def __init__(self, name: str, age: int, weight: str):
        self.name = name           # Assign the provided name to the instance variable
        self.age = age             # Assign the provided age to the instance variable
        self.weight = weight     # Assign the provided country to the instance variable

    # Method to return a string representation of the Person object
    def __str__(self) -> str:
        # Step 8: must RETURN (not print) this exact format
        return f"{self.name} is {self.age} years old and is from {self.country}."  # Format and return the string

    # Method to check if the person is eligible to vote (18 or older)
    def can_vote(self) -> bool:
        # Step 9: True if 18 or older, else False
        return self.age >= 18      # Return True if age is 18 or more, otherwise False
    
# Step 10: Example usage
# Inputs
person_1 = Person("Pete", 20, "230")
person_2 = Person("Emma", 17, "109")

# Outputs
print(person_1) # "Pete is 20 years old and is from USA."
print(person_1.can_vote()) # True
print(person_2) # "Emma is 17 years old and is from Brazil."
print(person_2.can_vote()) # False

class Student(Person):
    # Define the Student class that inherits from Person
    def __init__(self, name: str, age: int, country: str,):
        #call the init method in the child class
        Student.__init__(self, name, age, country)
        #set the student specific attributes of major and gpa
        self.major = major
        self.gpa = gpa

    def study(self)
        return f"{self.name} is studying {self.major}.- gpa: {self.gpa} -age: {self.age} -weight: {self.weight} _can vote: {self.can_vote()}"
class Staff(Person):
    # Delete pass and add your code here
    pass