import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestTransactions(BaseCase):
    @pytest.fixture
    def auth_data(self):
        email = BaseCase.random_email(
            "fixed_email@gmail.com")  # empty parameter for random email, or pass 'str' for fixed email
        password = "Qwerty123"
        data = {"email": email, "password": password}

        response = MyRequests.post(url="/auth/login", data=data)
        return {
            "accessToken": response.json().get('accessToken'),
            "refreshToken": response.json().get('refreshToken'),
            "sid": response.json().get('sid')
        }

    def test_post_transaction_income(self, auth_data):
        auth_headers = BaseCase.auth_headers(auth_data.get('accessToken'))
        auth_headers_negative = BaseCase.return_invalid_token(auth_data)
        empty_headers = {}
        json = {
            "description": "Income description",
            "amount": 100,
            "date": "2020-12-31",
            "category": "З/П"
        }
        json_negative = {"description": "Income description"}
        expected_fields = ["newBalance", "transaction"]

        response = MyRequests.post(url='/transaction/income', headers=auth_headers, data=json)
        Assertions.assert_status_code(response, 201)
        Assertions.assert_json_has_keys(response, expected_fields)
        Assertions.assert_negative_parameters('POST', '/transaction/income', json_negative, auth_headers, None, 400)
        Assertions.assert_negative_parameters('POST', '/transaction/income', json, empty_headers, None, 400)
        Assertions.assert_negative_parameters('POST', '/transaction/income', json, auth_headers_negative, None, 401)

    def test_get_transaction_income(self, auth_data):
        headers = BaseCase.auth_headers(auth_data.get('accessToken'))
        auth_headers_negative = BaseCase.return_invalid_token(auth_data)
        expected_fields = ["incomes"]

        response = MyRequests.get(url='/transaction/income', headers=headers)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_keys(response, expected_fields)
        Assertions.assert_negative_parameters('GET', '/transaction/income', None, {}, None, 400)
        Assertions.assert_negative_parameters('GET', '/transaction/income', None, auth_headers_negative, None, 401)

    def test_post_transaction_expense(self, auth_data):
        auth_headers = BaseCase.auth_headers(auth_data.get('accessToken'))
        auth_headers_negative = BaseCase.return_invalid_token(auth_data)
        empty_headers = {}
        json = {
            "description": "Expense description",
            "amount": 100,
            "date": "2020-12-31",
            "category": "Продукты"
        }
        json_negative = {"description": "Expense description"}
        expected_fields = ["newBalance", "transaction"]

        response = MyRequests.post(url='/transaction/expense', headers=auth_headers, data=json)
        Assertions.assert_status_code(response, 201)
        Assertions.assert_json_has_keys(response, expected_fields)
        Assertions.assert_negative_parameters('POST', '/transaction/income', json_negative, auth_headers, None, 400)
        Assertions.assert_negative_parameters('POST', '/transaction/income', json, empty_headers, None, 400)
        Assertions.assert_negative_parameters('POST', '/transaction/income', json, auth_headers_negative, None, 401)

    def test_get_transaction_expense(self, auth_data):
        headers = BaseCase.auth_headers(auth_data.get('accessToken'))
        auth_headers_negative = BaseCase.return_invalid_token(auth_data)
        expected_fields = ["expenses", "monthsStats"]

        response = MyRequests.get(url='/transaction/expense', headers=headers)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_keys(response, expected_fields)
        Assertions.assert_negative_parameters('GET', '/transaction/income', None, {}, None, 400)
        Assertions.assert_negative_parameters('GET', '/transaction/income', None, auth_headers_negative, None, 401)

    def test_get_transaction_period_data(self, auth_data):
        headers = BaseCase.auth_headers(auth_data.get('accessToken'))
        headers_negative = BaseCase.return_invalid_token(auth_data)
        params = {'date': '2020-12'}
        params_negative = {'d': '2020-12'}
        expected_fields = ["expenses", "incomes"]

        response = MyRequests.get(url='/transaction/period-data', headers=headers, params=params)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_keys(response, expected_fields)
        Assertions.assert_negative_parameters('GET', '/transaction/period-data', None, headers_negative, params, 401)
        Assertions.assert_negative_parameters('GET', '/transaction/period-data', None, headers_negative, params_negative, 400)
