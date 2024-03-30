from enumation import VisitorCategory

class Ticket:
    """Class to represent a ticket purchased by a visitor"""
    # This class is part of an aggregation relationship with the Visitor class.
    def __init__(self, numOfTickets, category):
        self.__numOfTickets = numOfTickets  # Private attribute to store the number of tickets
        self.__category = category  # Private attribute to store the visitor category for the ticket

    def calculate_total_price(self):
        # This function calculates the total price of the tickets based on the visitor category and number of tickets,

        # if condition to provide free tickets to certain categories
        if self.__category in [VisitorCategory.CHILD, VisitorCategory.STUDENT, VisitorCategory.TEACHER,
                               VisitorCategory.SENIOR]:
            return 0

        # Base price calculation for adults
        price_per_ticket = 63
        total_price = price_per_ticket * self.__numOfTickets  # Initial total price calculation

        # Applying VAT to the total price
        total_price += total_price * 0.05  # 5% VAT

        return total_price

"""
The Ticket class is designed to represent tickets purchased by visitors. 
Its part of an aggregation relationship with the Visitor class, where each 
Visitor object can hold multiple tickets, allowing the system to manage 
ticket sales and visitor entries in a structured manner. This class also 
includes a function for calculating the total price of tickets 
based on different conditions.
"""
