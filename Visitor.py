from Person import Person

class Visitor(Person):
    """Class representing a visitor, inheriting from the Person class.

    This class also shows an aggregation relationship with the Ticket class
    """

    def __init__(self, firstName, lastName, gender, phoneNumber, age, nationality, visitorId, email):
        # Initializing the parent class with common person attributes
        super().__init__(firstName, lastName, gender, phoneNumber)
        # Private attributes specific to a visitor
        self.__age = age
        self.__nationality = nationality
        self.__visitorId = visitorId
        self.__email = email
        # Protected attribute to store Ticket objects, demonstrating aggregation
        self._tickets = []

    # Setter and getter methods for private visitor specific attributes

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setNationality(self, nationality):
        self.__nationality = nationality

    def getNationality(self):
        return self.__nationality

    def setVisitorId(self, visitorId):
        self.__visitorId = visitorId

    def getVisitorId(self):
        return self.__visitorId

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def displayVisitor(self):
        # A function to display detials of the visitor
        print("Visitor Details:")
        print("Name:", self.getFirstName(), self.getLastName())
        print("Gender:", self.getGender().value)
        print("Phone Number:", self.getPhoneNumber())
        print("Age:", self.getAge())
        print("Nationality:", self.getNationality())
        print("Visitor ID:", self.getVisitorId())
        print("Email:", self.getEmail())
        print()

    def add_ticket(self, ticket):
        # This function adds a ticket to the visitor's list of tickets.
        self._tickets.append(ticket)

    def get_tickets(self):
        # This function returns a copy of the visitor's list of tickets.
        return self._tickets[:]

"""
The Visitor class, derived from the Person class, incorporates additional 
attributes relevant to museum visitors. It also demonstrates the use of 
aggregation through its relationship with the Ticket class, where a Visitor 
object can have multiple Ticket objects. 
"""

