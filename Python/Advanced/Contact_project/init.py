from User import User
from Token import Token
from Contact import Contact
import re


class Application:
    def __init__(self):
        self.users = []
        self.validTokens = []
        self.current_user = {
            "user_data": None,
            "token": ""
        }

    def start_app(self):
        continue_loop = True
        while continue_loop:
            self.print_messages()
            choice = self.get_user_input()
            if not self.check_user_is_login():
                if choice == "1":
                    self.handle_login()
                elif choice == "2":
                    self.handle_register()
                elif choice == "3":
                    print("Exiting...")
                    continue_loop = False
                else:
                    print("Invalid choice!")
            else:
                if choice == "1":
                    self.handle_add_contact()
                elif choice == "2":
                    self.handle_remove_contact()
                elif choice == "3":
                    self.handle_show_contacts()
                elif choice == "4":
                    self.handle_logout()
                else:
                    print("Invalid choice!")

    def print_messages(self):
        if not self.check_user_is_login():
            print("""
1- Login
2- Register
3- Exit
""")
        else:
            print("""
1- Add Contact
2- Remove Contact
3- My Contact
4- Logout
""")

    def get_user_input(self):
        return input("Enter your choice: ")

    def handle_login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = self.login(username, password)
        if user:
            print(f"Welcome {user.username}!")

    def handle_register(self):
        username = input("Enter new username: ")
        password = input("Enter password: ")
        if any(u.username == username for u in self.users):
            print("Username already exists!")
            return
        user = User(username, password)
        self.users.append(user)
        print(f"User {username} registered successfully!")

    def login(self, username, password):
        user = None
        for u in self.users:
            if u.username == username:
                user = u
                break

        if user is None:
            print("User not found")
            return None

        if user.password != password:
            print("Wrong Password")
            return None

        # Generate token
        tknService = Token()
        token = tknService.generate_token(user=user)

        self.current_user["user_data"] = user
        self.current_user["token"] = token
        self.validTokens.append(token)

        return user

    def check_user_is_login(self):
        if self.current_user["token"] == "":
            return False

        current_user = self.get_user_from_token(self.current_user["token"])
        if current_user is None or self.current_user["token"] not in self.validTokens:
            return False

        return True

    def get_user_from_token(self, token):
        tknService = Token()
        return tknService.extract_user_from_token(token)

    # Contact handlers
    def handle_add_contact(self):
        user = self.current_user["user_data"]
        name = input("Enter contact name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        age = input("Enter age: ")
        try:
            contact = Contact(name, phone, email, age)
            result = user.add_contact(contact)
            print(result)
        except ValueError as e:
            print(e)

    def handle_remove_contact(self):
        user = self.current_user["user_data"]
        phone = input("Enter phone of contact to remove: ")
        contacts = user.get_contacts_by_phone(phone)
        if not contacts:
            print("Contact not found")
            return
        contact = contacts[0]
        result = user.remove_contact(contact)
        print(result)

    def handle_show_contacts(self):
        user = self.current_user["user_data"]
        if not user.contacts:
            print("No contacts found")
            return
        print("My Contacts:")
        for c in user.contacts:
            print(
                f"Name: {c.name}, Phone: {c.phone}, Email: {c.email}, Age: {c.age}")

    def handle_logout(self):
        token = self.current_user["token"]
        if token in self.validTokens:
            self.validTokens.remove(token)
        self.current_user = {"user_data": None, "token": ""}
        print("Logged out successfully!")


# Run the application
app = Application()
app.start_app()
