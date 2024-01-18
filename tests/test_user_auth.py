import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserAuth(BaseCase):
    @pytest.fixture
    def auth_data(self):
        email = BaseCase.random_email(
            "fixed_email@gmail.com")  # empty parameter for random email, or pass str for fixed email
        password = "Qwerty123"
        data = {"email": email, "password": password}

        response = MyRequests.post('/auth/login', data)
        return {
            "accessToken": response.json().get('accessToken'),
            "refreshToken": response.json().get('refreshToken'),
            "sid": response.json().get('sid'),
            "email": email,
            "password": password
        }

    def test_auth_login(self, auth_data):
        expected_fields = ["accessToken", "refreshToken", "sid", "userData", "accessToken"]
        json = {"email": auth_data.get('email'), "password": auth_data.get('password')}

        response = MyRequests.post("/auth/login", json)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_keys(response, expected_fields)

    def test_auth_refresh(self, auth_data):
        auth_headers = BaseCase.auth_headers(auth_data.get('refreshToken'))
        sid = {"sid": auth_data.get('sid')}

        response = MyRequests.post("/auth/refresh", sid, auth_headers)
        Assertions.assert_status_code(response, 200)

    def test_auth_logout(self, auth_data):
        auth_headers = BaseCase.auth_headers(auth_data.get('accessToken'))

        response = MyRequests.post("/auth/logout", None, auth_headers)
        Assertions.assert_status_code(response, 204)

    def test_get_user_info(self, auth_data):
        auth_headers = BaseCase.auth_headers(auth_data.get('accessToken'))
        expected_fields = ["email", "balance", "transactions"]

        response = MyRequests.get("/user", None, auth_headers)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_keys(response, expected_fields)

    # def test_delete_transaction_expense(self, auth_data):
    #     auth_headers = BaseCase.auth_headers(auth_data.get('accessToken'))
    #
    #     response = MyRequests.delete('/transaction/659478aeeb03bb3d988035e1', None, auth_headers)
    #     Assertions.assert_status_code(response, 200)


