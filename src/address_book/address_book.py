from contact import Contact


# Class to initialize the list, add the details of the contacts in the list and display it
class AddressBook:
    """
        To initialize the list

        Parameters:
            self: Default parameter in the method inside the class

        Returns:
            None
    """

    def __init__(self):
        self.contacts = []

    """
        To add the detials of the contact into the list
        
        Parameters:
            self: Default parameter
            contact: The list in which the details of the contact get stored
            
        Returns:
            None
    """

    def add_contact(self, contact):
        self.contacts.append(contact)

    """
        To take the input from the user
        
        Parameters:
            self: Default parameter
            
        Returns:
            None
    """

    def add_contact_from_input(self):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip_code = input("Enter Zip Code: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
        self.add_contact(contact)

    """
        Displaying the contacts that has been added into the list
        
        Parameters:
            self: Default parameter
            
        Returns:
            None
    """

    def display_contacts(self):
        for contact in self.contacts:
            print("First Name:", contact.first_name)
            print("Last Name:", contact.last_name)
            print("Address:", contact.address)
            print("City:", contact.city)
            print("State:", contact.state)
            print("Zip Code:", contact.zip_code)
            print("Phone Number:", contact.phone_number)
            print("Email:", contact.email)
            print("--------------------")
