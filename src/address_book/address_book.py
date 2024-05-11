class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

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
