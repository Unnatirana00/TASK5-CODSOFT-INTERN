
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"Name: {self.name}, Number: {self.number}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        contact = Contact(name, number)
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_all_contacts(self):
        if self.contacts:
            print("All Contacts:")
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts available.")

    def search_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact.name == name:
                print("Contact found:")
                print(contact)
                found = True
                break
        if not found:
            print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter number: ")
            contact_book.add_contact(name, number)
        elif choice == '2':
            contact_book.view_all_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()