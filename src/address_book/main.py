from address_book import AddressBook

"""
    Main method to take the details, put it into the address book and displays it
    
    Parameters:
        None
        
    Returns:
        None
"""


def main():
    address_book = AddressBook()
    address_book.add_contact_from_input()
    address_book.display_contacts()


#To run the main method
if __name__ == "__main__":
    main()
