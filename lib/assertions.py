from requests import Response
from lib.my_requests import MyRequests
import json


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"RESPONSE IS NOT IN JSON FORMAT. RESPONSE TEXT IS: '{response.text}'"

        assert name in response_as_dict, f"RESPONSE JSON DOESN'T HAVE KEY '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, value_name):
        try:
            response_as_dict = response.json()
        except ValueError as e:
            assert False, f"RESPONSE IS NOT IN JSON FORMAT. RESPONSE IS: '{Response}'"

        assert value_name in response_as_dict, f"RESPONSE DOESN'T HAS THE KEY: '{value_name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response = response.json()
        except ValueError as e:
            assert False, f"RESPONSE IS NOT IN JSON FORMAT. RESPONSE IS: '{Response}'"

        for name in names:
            assert name in response, f"RESPONSE DOESN'T HAVE KEY '{name}'"

    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"UNEXPECTED STATUS CODE. ACTUAL: '{response.status_code}' EXPECTED: '{expected_status_code}'"

    @staticmethod
    def assert_negative_parameters(method, url, data, headers, params, expected_status_code):
        if method == 'GET':
            response = MyRequests.get(url, None, headers, None, params)
        elif method == 'POST':
            response = MyRequests.post(url, data, headers)
        elif method == 'PATCH':
            response = MyRequests.patch(url, data, headers)
        elif method == 'PUT':
            response = MyRequests.put(url, data, headers)
        elif method == 'DELETE':
            response = MyRequests.delete(url)
        else:
            raise Exception(f"BAD HTTP METHOD '{method}' WAS RECEIVED")

        assert response.status_code == expected_status_code, \
            f"UNEXPECTED STATUS CODE. ACTUAL: '{response.status_code}' EXPECTED: '{expected_status_code}'"