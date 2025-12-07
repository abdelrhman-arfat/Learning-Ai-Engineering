import re


class Contact:
    def __init__(self, name, phone, email, age):
        self.name = name
        self.phone = phone
        #  check email is valid or not :
        regex = re.search(
            "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", email)
        if regex:
            self.email = email
        else:
            raise ValueError("Invalid Email")
        self.email = email
        self.age = age
