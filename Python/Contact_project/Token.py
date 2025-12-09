import base64
import random
import string


class Token:
    def __init__(self):
        pass

    def generate_token(self, user):
        if (user == "" or user == None):
            return
        rand_number = random.randint(1000, 9999)
        rand_chars = ''.join(random.choices(
            string.ascii_letters + string.digits, k=8))
        #  encode user data:
        encode = self.encode_base64(user.username)
        return f"token@{encode}_{rand_chars}{rand_number}"

    def extract_user_from_token(self, token):
        if (token == "" or token == None):
            return
        #  decode user data:
        data = token.split("@")[1]
        user_phone = data.split("_")[0]
        decode = self.decode_base64(user_phone)
        return decode

    def encode_base64(self, data):
        encoded = base64.b64encode(data.encode()).decode()
        return encoded

    def decode_base64(self, encoded):
        return base64.b64decode(encoded.encode()).decode()
