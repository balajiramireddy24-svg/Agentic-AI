#Day 29 --> Revision

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully.")

    elif choice == "2":
        if contacts:
            print("\nContacts:")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")
        else:
            print("No contacts found.")

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print(f"{search} : {contacts[search]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")