from Person import Person

class Employee(Person):
    """Class represnting an employee, inheriting from the Person class"""

    def __init__(self, firstName, lastName, gender, phoneNumber, employeeID, department, position):
        # Initializing the parent class with common person attributes
        super().__init__(firstName, lastName, gender, phoneNumber)
        # Employee specific attributes (private)
        self.__employeeID = employeeID
        self.__department = department
        self.__position = position

    # Setter and getter methods for employee specific attributes

    def setEmployeeID(self, employeeID):
        self.__employeeID = employeeID

    def getEmployeeID(self):
        return self.__employeeID

    def setdepartment(self, department):
        self.__department = department

    def getdepartment(self):
        return self.__department

    def setPosition(self, position):
        self.__position = position

    def getEmail(self):
        return self.__position

    def displayEmployee(self):
        print("Employee Details:")
        print("Name:", self.getFirstName(), self.getLastName())
        print("Gender:", self.getGender().value)
        print("Phone Number:", self.getPhoneNumber())
        print("Employee ID:", self.getEmployeeID())
        print("Department:", self.getdepartment())
        print("Position:", self.getEmail())
        print()


"""
The Employee class extends the Person class, inheriting its attributes and methods 
while adding employee-specific details This class indicates the concept of inheritance, 
allowing it to reuse common personal information while focusing on the unique aspects 
of an employee's role within the museum.
"""