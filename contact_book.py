contact_book = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact_book[name] = {"Phone": phone, "Email": email}
    print(f"✅ Contact for {name} added.\n")

def view_contacts():
    if not contact_book:
        print("📭 No contacts found.\n")
        return
    for name, info in contact_book.items():
        print(f"👤 {name}\n📞 {info['Phone']}\n📧 {info['Email']}\n")

def update_contact():
    name = input("Enter the name to update: ")
    if name in contact_book:
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        contact_book[name] = {"Phone": phone, "Email": email}
        print(f"🔄 Contact for {name} updated.\n")
    else:
        print("❌ Contact not found.\n")

def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"🗑️ Contact for {name} deleted.\n")
    else:
        print("❌ Contact not found.\n")

def menu():
    while True:
        print("===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option (1–5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("📕 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1–5.\n")

menu()
