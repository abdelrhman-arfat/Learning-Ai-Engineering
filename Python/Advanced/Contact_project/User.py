
class User:
    def __init__(self, username, password):
        self.username = username
        # Hashing password is better or using hash in real world projects
        self.password = password
        self.contacts = []

    def add_contact(self, contact):
        phone = contact.phone
        if self.get_contacts_by_phone(phone):
            return "Contact Already Exists"
        self.contacts.append(contact)
        return "Contact Add Successfully"

    def remove_contact(self, contact):
        phone = contact.phone
        if not self.get_contacts_by_phone(phone):
            return "Contact Not Found"
        self.contacts.remove(contact)
        return "Contact Removed Successfully"

    def get_contacts_by_phone(self, phone):
        return [contact for contact in self.contacts if contact.phone == phone]
