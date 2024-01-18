from requests import Response
from datetime import datetime
import string
import random


class BaseCase:

    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"CANNOT FIND COOKIE WITH THE NAME {cookie_name} IN THE LAST RESPONSE"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"CANNOT FIND HEADER WITH THE NAME {header_name} IN THE LAST RESPONSE"
        return response.headers[header_name]

    @staticmethod
    def random_email(email=None):
        if email is None:
            base_part = "qwerty"
            domain = "gmail.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            return f"{base_part}{random_part}@{domain}"
        else:
            return str(email)

    @staticmethod
    def auth_headers(token):
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def return_invalid_token(auth_data):
        return {"Authorization": "InvalidToken " + auth_data["accessToken"]}

    @staticmethod
    def generate_password(length, use_latin=True, use_cyrillic=False):
        latin_chars = string.ascii_letters
        cyrillic_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

        available_chars = ""
        if use_latin:
            available_chars += latin_chars
        if use_cyrillic:
            available_chars += cyrillic_chars

        password = ''.join(random.choice(available_chars) for _ in range(length))
        return password
