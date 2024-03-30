from enumation import EventType
from enumation import EventLocation

class Event:
    """Class to represent an event in the museum"""
    def __init__(self, name, event_type: EventType, location: EventLocation, start_date, end_date):
        # Initialize event attributes
        self.name = name
        self.event_type = event_type
        self.location = location
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        # Returning a string representation of the event
        return f"Event: {self.name}, Type: {self.event_type.value}, Location: {self.location.value}, Dates: {self.start_date} to {self.end_date}"


"""
This class models events held within the museum, and its utilized within 
a composition relationship by the Museum class, which contains and manages 
multiple Event objects. This relationship indicates that events are 
integral parts of the museum's offerings. 
"""