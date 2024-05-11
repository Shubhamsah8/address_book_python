from contact import Contact
from address_book import AddressBook

# Created an AddressBook object
address_book = AddressBook()

# Feeding the details of the contact
contact1 = Contact("Shubham", "Sah", "Malad", "Mumbai", "Maharashtra", "400097", "8779817254", "shubhamsah086@gmail.com")

address_book.add_contact(contact1)

address_book.display_contacts()
