from enum import Enum

# Enumeration for Gender
class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"

# Enumeration for visitor catagory
class VisitorCategory(Enum):
    ADULT = "adult"
    CHILD = "child"
    STUDENT = "student"
    TEACHER = "teacher"
    SENIOR = "senior"

# Enumeration for event type
class EventType(Enum):
    EXHIBITION = "Exhibition"
    TOUR = "Tour"
    SPECIAL_EVENT = "Special Event"


# Enumeration for event location
class EventLocation(Enum):
    PERMANENT_GALLERIES = "Permanent Galleries"
    EXHIBITION_HALLS = "Exhibition Halls"
    OUTDOOR_SPACES = "Outdoor Spaces"

