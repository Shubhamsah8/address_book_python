from contact import Contact
from address_book import AddressBook

address_book = AddressBook()


def user_contact_info():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    address = input("Enter the address: ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")
    zip_code = input("Enter the zip code: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email: ")

    contact1 = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
    return address_book.add_contact(contact1)


no_of_details = int(input("Enter the number of details of contact: "))

for i in range(no_of_details):
    user_contact_info()

print("\n-----------------------------")
address_book.display_contacts()
print("\n-----------------------------")