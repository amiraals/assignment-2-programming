
class Person:
    """Class to represent a person"""

    def __init__(self, firstName, lastName, gender, phoneNumber):
        # Initialization of person attributes (note that they are all protected since this ia the parent class)
        self._firstName = firstName
        self._lastName = lastName
        self._gender = gender
        self._phoneNumber = phoneNumber

    # Setter and getter methods for person attributes

    def setFirstName(self, firstName):
        self._firstName = firstName

    def getFirstName(self):
        return self._firstName

    def setLastName(self, lastName):
        self._lastName = lastName

    def getLastName(self):
        return self._lastName

    def setGender(self, gender):
        self._gender = gender

    def getGender(self):
        return self._gender

    def setPhoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber

    def getPhoneNumber(self):
        return self._phoneNumber




"""
This class is designed to be a parent class, showcasing the use of inheritance. 
It provides a base set of attributes and methods that are common across both employees 
and visitors of the museum, ensuring code reuse. The inheritance relationship is implemented 
by having subclasses (Employee and Visitor) extend the Person class, and so inheriting its p
roperties and methods while also introducing role-specific attributes and functionalities.
"""