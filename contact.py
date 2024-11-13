print("This is a Contact Booking System based on Command Line")
print("Enter 1 for Add Contact, 2 for View Contacts, 3 for Search, 4 for Update, 5 for Delete, 6 to Exit")

contacts = []

while True:
    try:
        user_input = int(input("\nEnter your choice: "))
        
        match user_input:
            # Case 1: Add Contact
            case 1:
                name_of_contact = input("Enter name of contact: ")
                try:
                    no_of_contact = int(input("Enter contact number: "))
                except ValueError:
                    print("Invalid phone number. Please enter numeric values.")
                    continue
                User_email = input("Enter your email: ")
                
                new_contact = {"name": name_of_contact, "phone": no_of_contact, "email": User_email}
                contacts.append(new_contact)
                print("Contact added successfully!")
            
            # Case 2: View Contacts
            case 2:
                if not contacts:
                    print("No contacts available.")
                for person in contacts:
                    print(person)
            
            # Case 3: Search Contact
            case 3:
                user_search = input("Enter name to search: ")
                found = False
                for person in contacts:
                    if person["name"].lower() == user_search.lower():
                        print("User found:", person)
                        found = True
                        break
                if not found:
                    print("This person is not available in contacts.")
            
            # Case 4: Update Contact
            case 4:
                update_name = input("Enter the name of the person whose details you want to update: ")
                found = False
                for updates in contacts:
                    if updates["name"].lower() == update_name.lower():
                        new_name = input("Input new name: ")
                        try:
                            new_num = int(input("Enter new phone number: "))
                        except ValueError:
                            print("You entered an invalid number.")
                            continue
                        new_email = input("Input new email: ")
                        
                        updates["name"] = new_name
                        updates["phone"] = new_num
                        updates["email"] = new_email
                        print("Updated successfully!")
                        found = True
                        break
                if not found:
                    print("The entered name isn't in the contacts.")
            
            # Case 5: Delete Contact
            case 5:
                delete_name = input("Enter the name of the person you want to delete: ")
                found = False
                for person in contacts:
                    if person["name"].lower() == delete_name.lower():
                        contacts.remove(person)
                        print(f"Contact '{delete_name}' deleted successfully!")
                        found = True
                        break
                if not found:
                    print("The entered name isn't in the contacts.")
            
            # Case 6: Exit
            case 6:
                print("Exiting... Goodbye!")
                break
            
            # Default Case: Invalid Option
            case _:
                print("Invalid choice! Please enter a number from 1 to 6.")
    
    except ValueError:
        print("Please enter a valid number.")
