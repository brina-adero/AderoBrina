class ContactManager:
    def __init__(self):
        # We use a dictionary where the key is the contact's name 
        # and the value is another dictionary containing phone and email.
        self.contacts = {}

    def validate_phone(self, phone):
        phone = phone.strip()
        
        # If it starts with +, we test the rest of the string
        test_phone = phone
        if phone.startswith('+'):
            test_phone = phone[1:]
            
        # Replace hyphens to check if only digits are left
        clean_phone = test_phone.replace('-', '')
        
        if clean_phone.isdigit() and len(clean_phone) > 0:
            return True
        else:
            return False

    def validate_email(self, email):
        if "@" in email and "." in email:
            return True
        return False

    def display_results(self, results_list):
        if not results_list:
            print("\n[!] No contacts found matching that criteria.")
            return

        print("\n" + "="*50)
        print(f"{'Name':<15} | {'Phone':<18} | {'Email':<25}")
        print("="*50)
        for name, info in results_list:
            print(f"{name:<15} | {info['phone']:<18} | {info['email']:<25}")
        print("="*50 + "\n")

    def add_contact(self, name, phone, email):
        #Adds a new contact after validating phone and email.
        name = name.strip()
        if not name:
            print("[Error] Name cannot be empty!")
            return

        if name in self.contacts:
            print(f"[Error] Contact with the name '{name}' already exists.")
            return

        # Validate Phone
        if not self.validate_phone(phone):
            print("[Error] Invalid phone number! Use only digits and hyphens (e.g., +256-701-000).")
            return

        # Validate Email
        if not self.validate_email(email):
            print("[Error] Invalid email address! Must contain '@' and '.'")
            return

        # Save to our dictionary if valid
        self.contacts[name] = {"phone": phone, "email": email}
        print(f"[Success] Contact '{name}' added successfully!")

    def view_contact(self, name):
        #Displays a single contact's details.
        name = name.strip()
        if name in self.contacts:
            info = self.contacts[name]
            print("\n--- Contact Details ---")
            print(f"Name:  {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}\n")
        else:
            print(f"[Error] Contact '{name}' not found.")

    def update_contact(self, name, new_phone, new_email):
        #Updates an existing contact's phone and email with validation.
        name = name.strip()
        if name not in self.contacts:
            print(f"[Error] Contact '{name}' does not exist.")
            return

        # Validate New Phone
        if not self.validate_phone(new_phone):
            print("[Error] Invalid phone number! Update canceled.")
            return

        # Validate New Email
        if not self.validate_email(new_email):
            print("[Error] Invalid email address! Update canceled.")
            return

        # Update the details
        self.contacts[name]["phone"] = new_phone
        self.contacts[name]["email"] = new_email
        print(f"[Success] Contact '{name}' updated successfully!")

    def delete_contact(self, name):
        #Deletes a contact from the system.
        name = name.strip()
        if name in self.contacts:
            del self.contacts[name]
            print(f"[Success] Contact '{name}' deleted successfully!")
        else:
            print(f"[Error] Contact '{name}' not found.")

    def search_contacts(self, query):
        #Searches contacts by matching query against name, phone, or email.
        query = query.lower().strip()
        matched_results = []

        for name, info in self.contacts.items():
            # Check if query is in name, phone, or email string
            if (query in name.lower() or 
                query in info['phone'] or 
                query in info['email'].lower()):
                matched_results.append((name, info))

        # Display the results using our helper layout function
        self.display_results(matched_results)

    def list_all_contacts(self):
        #Converts the entire dictionary into a list of tuples to pass to our display helper.
        all_results = list(self.contacts.items())
        self.display_results(all_results)


def main():
    # Instantiate the manager object
    manager = ContactManager()

    # Pre-populate with a couple of student dummy contacts for testing
    manager.add_contact("Allan", "+256-701-111222", "allan@mail.com")
    manager.add_contact("Bella", "+256-772-333444", "bella@mail.com")

    while True:
        print("=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ").strip()

        if choice == '1':
            print("\n--- Add New Contact ---")
            name = input("Enter Name: ")
            phone = input("Enter Phone (e.g. +256-701-123): ")
            email = input("Enter Email: ")
            manager.add_contact(name, phone, email)

        elif choice == '2':
            print("\n--- View Contact ---")
            name = input("Enter the exact name to view: ")
            manager.view_contact(name)

        elif choice == '3':
            print("\n--- Update Contact ---")
            name = input("Enter the exact name to update: ")
            new_phone = input("Enter New Phone: ")
            new_email = input("Enter New Email: ")
            manager.update_contact(name, new_phone, new_email)

        elif choice == '4':
            print("\n--- Delete Contact ---")
            name = input("Enter the exact name to delete: ")
            manager.delete_contact(name)

        elif choice == '5':
            print("\n--- Search Contacts ---")
            query = input("Enter search keyword (name, phone, or email): ")
            manager.search_contacts(query)

        elif choice == '6':
            print("\n--- All System Contacts ---")
            manager.list_all_contacts()

        elif choice == '7':
            print("\nThank you for using the Contact Manager! Goodbye.")
            break

        else:
            print("\n[!] Invalid choice! Please enter a number from 1 to 7.\n")


# This ensures the program runs when executing the script directly
if __name__ == "__main__":
    main()
