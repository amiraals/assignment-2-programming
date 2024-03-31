from Visitor import Visitor
from enumation import Gender
from Employee import Employee
from Museum import Museum
from Ticket import Ticket
from Exhibition import Artwork
from Exhibition import Exhibition
from enumation import VisitorCategory


def mainInfo():
    print("Welcome to the Louvre Museum system!")
    print("Please note that fields marked with an (*) are mandatory and must be filled out; all other fields are optional.")
    while True:
        # Ask user to create a new Employee or Visitor
        choice = input("\nEnter -v- if you're a Visitor, and -e- if you're an Employee:* ").upper()
        if choice not in ['E', 'V']:
            # Handling invalid input for choice
            print("Please enter 'E' for Employee or 'V' for Visitor.")
            continue

        # Collecting common information for both Employee and Visitor
        firstName = input("First Name:* ")
        while not firstName:  # Check for empty input
            print("This field cannot be empty. Please enter a valid First Name.")
            firstName = input("First Name: ")

        lastName = input("Last Name:* ")
        while not lastName:  # Check for empty input
            print("This field cannot be empty.. Please enter a valid Last Name.")
            lastName = input("Last Name: ")


        # Looping until a valid gender is provided
        while True:
            gender_input = input("Gender (Male/Female):* ").strip().upper()
            try:
                # Attempting to convert the input to the Gender enum
                gender = Gender[gender_input]
                break  # Will break out of the loop if its successful
            except KeyError:
                # For any KeyError if gender_input is not a valid key in Gender enum
                print("Invalid gender. Please enter 'Male' or 'Female'.")


        phoneNumber = input("Phone Number:* ")
        while not phoneNumber:  # Check for empty input
            print("This field cannot be empty. Please enter a valid Phone Number.")
            phoneNumber = input("Phone Number: ")

        if choice == 'E':
            # Specific information for Employee
            employeeID = input("Employee ID:* ")
            while not employeeID:
                print("This field cannot be empty. Please enter a valid Employee ID.")
                employeeID = input("Employee ID: ")

            department = input("Department:* ")
            while not department:
                print("This field cannot be empty. Please enter a valid Department.")
                department = input("Department: ")

            position = input("Position: ")

            # Creating Employee objectt
            employee = Employee(firstName, lastName, gender, phoneNumber, employeeID, department, position)
            # Displaying employee details
            employee.displayEmployee()
            # Goes to the empolyee specific function
            employee_system()
            break

        elif choice == 'V':
            while True:
                try:
                    age = int(input("Age:* "))
                    if age < 0:
                        print("Age cannot be negative. Please enter a positive integer.")
                    else:
                        break
                except ValueError:
                    # Handling non-integer inputs for age
                    print("Invalid age. Please enter a positive integer.")

            # Specific information for Visitor

            nationality = input("Nationality:* ")
            while not nationality:
                print("This field cannot be empty.. Please enter a valid Nationality.")
                nationality = input("Nationality: ")

            visitorId = input("Visitor ID:* ")
            while not visitorId:
                print("This field cannot be empty. Please enter a valid Visitor ID.")
                visitorId = input("Visitor ID:* ")
            email = input("Email: ")
            # Creating a Visitor object
            visitor = Visitor(firstName, lastName, gender, phoneNumber, age, nationality, visitorId, email)
            # Displaying visitor details
            visitor.displayVisitor()

            # Goes to the visitor specific function
            visitor_system(visitor)
            break


def visitor_system(visitor):
    print("Your details are submitted successfully.")
    while True:
        try:
            # Ask the visitor if they want to exit or proceed with booking tickets
            user_choice = int(input("\nEnter 0 to exit or 1 to proceed with booking tickets:* "))

            if user_choice == 0:
                # If the user chooses to exit the system
                print("\nExiting system. Thank you for using our services!")
                break
            elif user_choice == 1:
                # If the user chooses to proceed with booking tickets
                purchase_tickets(visitor)  # Calling the function that handles ticket purchase

                while True:
                    try:
                        event_choice = int(input("\nEnter 0 to exit or 1 to get the list of events of the week:* "))
                        if event_choice == 1:
                            # If the user chooses to view the list of events
                            display_events(museum)  # Calling the function that displays events
                            print("\nThank you for using our services! Have a great day.")
                            break
                        elif event_choice == 0:
                            print("\nThank you for using our services! Have a great day.")
                            break
                        else:
                            print("Invalid option selected. Please enter '0' or '1'.")
                    except ValueError:
                        print("Invalid option selected. Please enter '0' or '1'.")
                break

        except ValueError:
            # Handling invalid inputs
            print("Invalid option selected.")


def employee_system():
    while True:
        try:
            # Asking the employee if they want to exit or continue to the exhibition system
            user_choice = int(input("Enter 0 to exit or 1 to enter the exhibition system:* "))

            if user_choice == 0:
                # If the user chooses to exit
                print("Exiting system.")
                break
            elif user_choice == 1:
                # If the user chooses to proceed to exhibition system
                manage_exhibitions()  # Calling the function that manages the exhibition system
                print("Thank you for using our services. Exiting system.")
                break

        except ValueError:
            # Handling invalid inputs
            print("Invalid option selected. Please enter '0' or '1'.")



def purchase_tickets(visitor):
    total_price = 0
    # Asking the user for the number of tickets they wish to get
    numOfTickets = int(input("\nHow many tickets would you like to purchase?* "))

    # Looping through the number of tickets to process each one
    for _ in range(numOfTickets):
        while True:  # Keep on asking for the ticket category until getting valid one
            category_input = input("Enter ticket category (Adult/Child/Student/Teacher/Senior):* ").upper()
            try:
                # Attempting to convert the user's category input into a VisitorCategory enum
                category = VisitorCategory[category_input]
                break
            except KeyError:
                # Handiling invalid user input
                print(f"Invalid category: {category_input}. Please enter a valid ticket category.")

        # Creating a new ticket object for the specified category
        ticket = Ticket(1, category)  # Here i asumes there is 1 ticket per category input
        # Adding the new ticket to the visitor's ticket list
        visitor.add_ticket(ticket)
        # Adding the price of the current ticket to the total price
        total_price += ticket.calculate_total_price()

    # After processing all tickets,  a discount is applied if more than 5 tickets were purchased (group discount)
    if numOfTickets > 5:
        discount = total_price * 0.5  # Calculating a 50% discount on the total price
        total_price -= discount  # Applying the discount to the total price

    print(f"Total price for {numOfTickets} tickets: {total_price:.2f} AED")


# Creating a Museum object
museum = Museum("Louvre Museum", 5)

def display_events(museum):
    print(f"Events at {museum.getName()}:")
    # Iterate over each event in the museum's 'events' list
    for event in museum._events:
        # Printing each event which relies on each Event object having a __str__ method defined
        print(event)



def manage_exhibitions():
    artworks = []  # Initializing an empty list to store artworks for a new exhibition
    exhibition_name = input("\nEnter the name of the exhibition: *")
    while not exhibition_name:
        print("Exhibition name cannot be empty. Please enter a valid Exhibition name.")
        exhibition_name = input("\nEnter the name of the exhibition: *")

    exhibition = Exhibition(exhibition_name, artworks)  # Creating an Exhibition object

    while True:
        try:
            choice = int(input("\nPress 1 to add an artwork, 2 to remove an artwork, or 3 to exit: *"))

            if choice == 1:
                # Add an artwork process
                print("\nEnter details for a new artwork.")
                title = input("Title:* ")
                while not title:
                    print("This field cannot be empty. Please enter a valid title")
                    title = input("Title:* ")
                artist = input("Artist:* ")
                while not artist:
                    print("This field cannot be empty. Please enter a valid artist name.")
                    artist = input("Artist:* ")
                creation_date = input("Creation Date (YYYY-MM-DD):* ")
                while not creation_date:
                    print("This field cannot be empty. Enter a valid date. ")
                    creation_date = input("Creation Date (YYYY-MM-DD):* ")
                artworks.append(Artwork(title, artist, creation_date))
                print("Artwork added.")
            elif choice == 2:
                # Remove an artwork process
                if not artworks:  # Checking if the list is empty
                    print("No artworks to remove.")
                    continue

                title = input("Enter the title of the artwork to remove:* ")
                while not title:
                    print("This field cannot be empty. Please enter a valid title.")
                    title = input("Enter the title of the artwork to remove:* ")

                # Attempting to remove the artwork 
                try:
                    if exhibition.remove_artwork(title):
                        print("Artwork removed.")
                    else:
                        print("Artwork not found. Please check the title and try again.")
                except ValueError:
                    print("Artwork not found. Please check the title and try again.")

            elif choice == 3:
                print("Existing System")
                break
            else:
                # Handling the case if the choice is an integer but not 1, 2, or 3
                print("Invalid choice, please try again.")

        except ValueError:
            # Handling the case if the input is not an integer
            print("Invalid input. Please enter a number (1, 2, or 3).")

    # Displaying the exhibition and its artworks
    if artworks:
        exhibition.display_info()
    else:
        print(f"Exhibition: {exhibition_name} has no artworks to display.")


mainInfo()

