import re

contacts = {1234567890: {"Name" : "Shrek", "Phone number" : 1234567890, "Email" : "swampdaddy@swampdaddy.edu", "Additional info" :  "GET OUTTA MY SWAMP!!"}}

def cli():      # This is the main menu
    while True:
        user_input = input('''      
Welcome to the Contact Management System!

📞 Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import previous contacts
8. Quit
        
    ''')
        if user_input == "1":
            add_contact()
        elif user_input == "2":
            edit_contact()
        elif user_input == "3":
            delete_contact()
        elif user_input == "4":
            search_contacts()
        elif user_input == "5":
            display_contacts()
        elif user_input == "6":
            export_contacts()
        elif user_input == "7":
            import_contacts()
        elif user_input == "8":
            break
        else:
            input("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")

        

def add_contact():
    try:
        name = input("\nWhat is the name of your new contact? ")
        phone_number = input(f"What is {name}'s phone number? ")
        phone_number = re.sub(r'\D', '', phone_number)   
        phone_number = re.search(r"\d{10}", phone_number).group()
        if phone_number == None:
            input("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
            return
        email = input(f"What is {name}'s email? ")
        email = re.search(r"[A-Za-z.-_]+@[A-Za-z0-9.-_]+.[A-Z|a-z.-]{2,}" , email).group()
        if email ==  None:
            input("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
            return
        additional_information = input("Additional information: ")
        contacts.update({phone_number : {"Name" : name, "Phone number" : phone_number, "Email" : email, "Additional info" : additional_information}})
        input("\n✨ Your contact has been added! ✨")
    except AttributeError:
        input("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")




def edit_contact():
    try:
        phone_number = (input("\nWhat is the phone number of the contact you're trying to edit? "))        #Finds the contact they are trying to edit
        phone_number = re.sub(r'\D', '', phone_number)       
        phone_number = re.search(r"\b\d{10}\b", phone_number).group()
        if phone_number == None:
            input("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
            return
        c = 1
        contacts[phone_number]
        print("\nWhat would you like to edit about the contact?\n")
        for key in contacts[phone_number].keys():
            print(f"{c}: {contacts[phone_number][key]}")       #lists details of the contact
            c += 1
        edit = input("")

        if edit == "1":
            edit = "Name"
        elif edit == "2":
            edit = "Phone number"
        elif edit == "3":
            edit = "Email"
        elif edit == "4":
            edit = "Additional info"
        else:
            input("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
            return
        new_value = input(f"""\n{contacts[phone_number]["Name"]}'s {edit} currently is {contacts[phone_number][edit]}
What would you like to change it too?

""")                            

        contacts[phone_number][edit] = new_value
        input(f"This contacts {edit} has been changed to {contacts[phone_number][edit]}")

        if edit == "Phone number":
            contacts[new_value] = contacts[phone_number]
            del contacts[phone_number]
    except AttributeError:
        input("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
    except KeyError:
        input(f"No contact exists under the phone number {phone_number}")

def delete_contact():
    phone_number = input("\nWhat is the phone number of the contact you would like to delete? ")
    try:
        user_input = input(f"Are you sure you want to delete {contacts[phone_number]["Name"]}?(y/n) ")
        if user_input == "y":
            print(f"{contacts[phone_number]["Name"]}'s contact has been deleted 🪚 ")
            del contacts[phone_number]
            input("")
        else:
            input("The contact was not deleted.")
    except (ValueError, KeyError):
        input("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")

def search_contacts():
    try:
        phone_number = input("What is the phone number of the contact you are looking for?🔭 ")
        phone_number = re.sub(r'\D', '', phone_number)       
        phone_number = re.search(r"\b\d{10}\b", phone_number).group()
        if phone_number == None:
            input("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
            return

        for key in contacts[phone_number].keys():
            print(f"{key}: {contacts[phone_number][key]}")  
        input("")     #lists details of the contact
    except (AttributeError, KeyError):
        input("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")

        
def display_contacts():
    for key in contacts.keys():
        print(f"{contacts[key]["Name"]}: {contacts[key]["Phone number"]}")
    input("")

def export_contacts():
    user_input = input(f"Are you sure you want to export your contacts? (y/n) ")
    if user_input == "y":
        with open("contacts/contacts.txt", "a") as file, open("contacts/contacts.txt", "w") as overrite:
            overrite.write("")
            for key in contacts.keys():
                file.write("{")
                file.write(f"'{key}': {contacts[key]}")
                file.write("}\n")
        input("Your contacts have been exported! ")
    else:
        input("Your contacts were NOT exported! ")
        return    

def import_contacts():
    user_input = input(f"Are you sure you want to import your contacts? (y/n) ")
    if user_input == "y":
        with open("contacts/contacts.txt", "r") as file:
            for line in file:
                var = eval(line)
                phone_number = re.search("[0-9]+", line).group()
                var[phone_number]["Phone number"] = var[phone_number]["Phone number"]
                var2 = {}
                var2[phone_number] = var[phone_number]
                del var
                contacts.update(var2)
        input("Your contacts have been imported! ")
    else:
        input("Your contacts were NOT imported! ")
        return    


           




cli()