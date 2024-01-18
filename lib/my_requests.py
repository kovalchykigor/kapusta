import requests
from lib.logger import Logger


class MyRequests():

    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None, params: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'POST', params)

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None, params: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'GET', params)

    @staticmethod
    def put(url: str, data:dict = None, headers: dict = None, cookies: dict = None, params: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'PUT', params)

    @staticmethod
    def patch(url: str, data:dict = None, headers: dict = None, cookies: dict = None, params: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'PATCH', params)

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None, params: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'DELETE', params)

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str, params: dict):

        url = f"https://kapusta-backend.goit.global{url}"

        if headers is None:
            headers = {}
        elif cookies is None:
            cookies = {}

        Logger.add_requests(url, data, headers, cookies, method)

        if method == 'GET':
            response = requests.get(url=url, headers=headers, params=params)
        elif method == 'POST':
            response = requests.post(url=url, headers=headers, json=data, cookies=cookies)
        elif method == 'PUT':
            response = requests.put(url=url, headers=headers, json=data, cookies=cookies)
        elif method == 'PATCH':
            response = requests.put(url=url, headers=headers, json=data, cookies=cookies)
        elif method == 'DELETE':
            response = requests.delete(url=url, headers=headers, params=data, cookies=cookies)
        else:
            raise Exception(f"BAD HTTP METHOD '{method}' WAS RECEIVED")

        Logger.add_response(response)

        return response