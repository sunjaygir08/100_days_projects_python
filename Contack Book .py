Contact = {}
def show_menu():
    print("\n========CONTACT BOOK MENU========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Edit Contact")
    print("6. Exit")
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    Contact[name] = {"Phone": phone, "Email": email}
    print(f"Contact '{name}' added successfully!")
def view_contact():
    if Contact:
        print("\n==== Contacts List ====")
        for name, details in Contact.items():
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
    else:
        print("No contacts found.")
def search_contact():
    name = input("Enter contact name to search: ")
    if name in Contact:
        details = Contact[name]
        print(f"Name: {name}")
        print(f"Phone: {details['Phone']}")
        print(f"Email: {details['Email']}")
    else:
        print(f"Contact '{name}' not found.")
def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in Contact:
        del Contact[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")
def edit_contact():
    name = input("Enter contact name to edit: ")
    if name in Contact:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        Contact[name] = {"Phone": phone, "Email": email}
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        edit_contact()
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print(" Invalid choice. Please enter a number between 1 and 6.")
    
