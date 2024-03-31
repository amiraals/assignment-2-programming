from enumation import EventType
from enumation import EventLocation

class Event:
    """Class to represent an event in the museum"""
    def __init__(self, name, event_type: EventType, location: EventLocation, start_date, end_date):
        # Initialize event attributes
        self.__name = name
        self.__event_type = event_type
        self.__location = location
        self.__start_date = start_date
        self.__end_date = end_date

    def __str__(self):
        # Returning a string representation of the event
        return f"Event: {self.__name}, Type: {self.__event_type.value}, Location: {self.__location.value}, Dates: {self.__start_date} to {self.__end_date}"


"""
This class models events held within the museum, and its utilized within 
a composition relationship by the Museum class, which contains and manages 
multiple Event objects. This relationship indicates that events are 
integral parts of the museum's offerings. 
"""
