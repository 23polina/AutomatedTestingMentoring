import requests


class Client:

    def __init__(self, base_url:str):
        """Create a client"""
        self.base_url = base_url

    def get_request(self, endpoint:str):
        """Send a GET request to base_url/endpoint."""
        return requests.get(f"{self.base_url}/{endpoint}", timeout=5)
