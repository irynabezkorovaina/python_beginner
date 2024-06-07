from contact import Contact
from contact_list import ContactList

if __name__ == '__main__':
    print('Task 19. Contact List')

    # Create an instance of ContactList to store the contacts
    contact_list = ContactList()

    while True:
        try:
            name = input('name: ')
            email = input('email: ')
            age = input('age: ')

            # Create a new Contact object with the provided details
            new_contact = Contact(name=name, email=email, age=age)
        except ValueError as e:
            # If there is a validation error, print the error message and continue the loop
            print(e)
            continue

        print('-' * 10)
        print(new_contact)
        print('-' * 10)

        # Append the new contact to the contact list
        contact_list.append(new_contact)
        proceed = input('add another one? (y/n): ')

        # Break the loop if the user does not want to add another contact
        if proceed != 'y':
            break

    # Display the contact list
    print("\nContact List:")
    for contact in contact_list:
        print(contact)
