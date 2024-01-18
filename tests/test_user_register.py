import pytest
from lib.base_case import BaseCase
from lib.my_requests import MyRequests
from lib.assertions import Assertions


class TestUserRegister(BaseCase):

    '''201 created'''
    def test_valid_data(self):
        email = BaseCase.random_email()
        password = BaseCase.generate_password(10, True, False)  # (len, latin, cyrillic)
        data = {"email": email, "password": password}

        response = MyRequests.post('/auth/register', data)
        Assertions.assert_status_code(response, 201)

        response_same_email = MyRequests.post('/auth/register', data)
        Assertions.assert_status_code(response_same_email, 409)  # 409 Provided email already exists

    '''400 Bad request (invalid request body)'''
    def test_invalid_data(self):
        valid_email = BaseCase.random_email()
        valid_password = BaseCase.generate_password(10, True, False)
        test_cases = [

            {"name": "Invalid data - invalid email key", "data": {"emli": valid_email, "password": valid_password}},
            {"name": "Invalid data - invalid password key", "data": {"email": valid_email, "pass": valid_password}},
            {"name": "Invalid data - missing email key", "data": {"password": valid_password}},
            {"name": "Invalid data - missing password key", "data": {"email": valid_email}},
            {"name": "Invalid data - empty data", "data": {}}
        ]

        for test_case in test_cases:
            response = MyRequests.post('/auth/register', test_case["data"])
            Assertions.assert_status_code(response, 400)




