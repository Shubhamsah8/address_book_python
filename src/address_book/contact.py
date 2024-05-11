#Class contact to initialize the details of the contact

class Contact:
    """
        Initializing the details of the contact

        Parameters:
            self: Default parameter for the method inside the class
            first_name (str): First name of the contact
            last_name (str): Last name of the user
            address (str): Address of the user
            city (str): City in which user live
            state (str): State in which user stay
            zip_code (str): Zip code of the address
            phone_number (str): Phone number of the user
            email (str): Email of the user

        Returns:
            None
    """

    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email
