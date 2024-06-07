from contact import Contact


class ContactList:
    def __init__(self):
        self.contacts = []

    def append(self, contact):
        if not isinstance(contact, Contact):  # Check if the contact is an instance of the Contact class
            raise ValueError('Invalid contact!')
        self.contacts.append(contact)  # Append the valid contact to the contacts list

    def __iter__(self):
        return iter(self.contacts)  # Return an iterator for the contacts list to support iteration
