from Event import Event
from enumation import EventType
from enumation import EventLocation
from datetime import datetime
import random

class Museum:
    """Class to represent a museum

    This class has a composition relationship with the Event class. """
    def __init__(self, name, num_events):
        # Initialize museum attributes
        self.__name = name
        self.__num_events = num_events
        self._events = self.create_events(num_events)

    # Setter and getter methods

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name


    def create_events(self, num_events):
        # This function uses the Event class's constructor to create Event objects with random types, locations, and dates.
        listEvents = []
        for i in range(num_events):
            name = f"Event {i + 1}"
            event_type = random.choice(list(EventType))
            location = random.choice(list(EventLocation))
            start_date = datetime(2024, 4, 1)
            end_date = datetime(2024, 5, 1)
            event = Event(name, event_type, location, start_date, end_date)
            listEvents.append(event)  # The Event objects are added to the events list attribute of the Museum class
        return listEvents

# Creating an instance of the Museum class
museum = Museum("Louvre Museum", 7)


"""
This class represents the museum itself, and demonstrates the concept
of composition through its relationship with the Event class, where 
the museum is composed of multiple events. This composition is
implemented by including a list of Event objects within the Museum class, 
enabling the museum to manage its events effectively.
"""
