# Cell 1: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

print("✅ Google Drive mounted successfully!")

# Cell 2: Your Complete Contact Book Application (Colab Version)

import csv
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# --- CONFIGURATION ---
# CRITICAL COLAB FIX: We define the path to save the file inside your Google Drive.
# This creates a file called 'contacts.csv' in your main "My Drive" folder.
DRIVE_PATH = '/content/drive/MyDrive/'
CSV_FILE = os.path.join(DRIVE_PATH, 'contacts.csv')


# --- OOP CLASS DEFINITION ---
class Contact:
    """A class to represent a single contact."""
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        """Converts the Contact object to a dictionary for saving."""
        return {'name': self.name, 'phone': self.phone, 'email': self.email}

    @classmethod
    def from_dict(cls, data):
        """Creates a Contact object from a dictionary."""
        # Handle cases where the email might be an empty string from the CSV
        email = data.get('email')
        return cls(data['name'], data['phone'], email if email else None)

    def display(self):
        """Prints the contact's details in a neat, colored format."""
        print(f"  {Style.BRIGHT}Name:  {self.name}")
        print(f"  Phone: {self.phone}")
        if self.email and self.email != 'None':
            print(f"  Email: {self.email}")
        print(Fore.CYAN + "-" * 30)

# --- DATA PERSISTENCE FUNCTIONS ---
def save_contacts(contacts_list):
    """Saves a list of Contact objects to the CSV file in Google Drive."""
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['name', 'phone', 'email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts_list:
            writer.writerow(contact.to_dict())

def load_contacts():
    """Loads contacts from the CSV file in Google Drive."""
    if not os.path.exists(CSV_FILE):
        return []
    
    contacts_list = []
    with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts_list.append(Contact.from_dict(row))
    print(Fore.GREEN + f"Loaded {len(contacts_list)} contacts from Google Drive.")
    return contacts_list

# --- CORE LOGIC FUNCTIONS ---
def add_contact(contacts_list):
    print(Fore.CYAN + "\n--- Add a New Contact ---")
    name = input("Enter name: ")
    for contact in contacts_list:
        if contact.name.lower() == name.lower():
            print(Fore.RED + f"Error: A contact named '{name}' already exists.")
            return
    phone = input("Enter phone number: ")
    email = input("Enter email (optional, press Enter to skip): ")
    new_contact = Contact(name, phone, email if email else None)
    contacts_list.append(new_contact)
    print(Fore.GREEN + f"\nSuccess! Contact for '{name}' added.")
    save_contacts(contacts_list)

def display_all_contacts(contacts_list):
    print(Fore.CYAN + "\n--- All Contacts ---")
    if not contacts_list:
        print("Your contact book is empty.")
        return
    for index, contact in enumerate(contacts_list, start=1):
        print(f"{Style.BRIGHT}{index}.")
        contact.display()

def search_contact(contacts_list):
    print(Fore.CYAN + "\n--- Search for a Contact ---")
    search_term = input("Enter a name or part of a name to search for: ").lower()
    found_contacts = [c for c in contacts_list if search_term in c.name.lower()]
    if not found_contacts:
        print(Fore.RED + f"No contacts found matching '{search_term}'.")
        return
    print(Fore.GREEN + f"\nFound {len(found_contacts)} contact(s):")
    for contact in found_contacts:
        contact.display()

def update_contact(contacts_list):
    print(Fore.CYAN + "\n--- Update a Contact ---")
    name_to_update = input("Enter the exact name of the contact to update: ")
    contact_to_update = None
    for contact in contacts_list:
        if contact.name.lower() == name_to_update.lower():
            contact_to_update = contact
            break
    if contact_to_update:
        print(f"\nUpdating contact for '{contact_to_update.name}'. Leave blank to keep current value.")
        new_phone = input(f"Enter new phone ({contact_to_update.phone}): ")
        if new_phone: contact_to_update.phone = new_phone
        new_email = input(f"Enter new email ({contact_to_update.email}): ")
        if new_email: contact_to_update.email = new_email
        print(Fore.GREEN + "Contact updated successfully!")
        save_contacts(contacts_list)
    else:
        print(Fore.RED + f"Contact '{name_to_update}' not found.")

def delete_contact(contacts_list):
    print(Fore.CYAN + "\n--- Delete a Contact ---")
    name_to_delete = input("Enter the exact name of the contact to delete: ")
    contact_to_delete = None
    for contact in contacts_list:
        if contact.name.lower() == name_to_delete.lower():
            contact_to_delete = contact
            break
    if contact_to_delete:
        contacts_list.remove(contact_to_delete)
        print(Fore.GREEN + f"Contact '{name_to_delete}' deleted successfully.")
        save_contacts(contacts_list)
    else:
        print(Fore.RED + f"Contact '{name_to_delete}' not found.")

# --- MAIN APPLICATION ---
def main():
    """Main function to run the contact management system in Colab."""
    contacts = load_contacts()
    while True:
        print(Style.BRIGHT + Fore.YELLOW + "\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1': add_contact(contacts)
        elif choice == '2': display_all_contacts(contacts)
        elif choice == '3': search_contact(contacts)
        elif choice == '4': update_contact(contacts)
        elif choice == '5': delete_contact(contacts)
        elif choice == '6':
            print(Fore.YELLOW + "Exiting program. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
