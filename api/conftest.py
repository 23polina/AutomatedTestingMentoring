import pytest

from api.client_api import Client

@pytest.fixture
def api_client() -> Client:
    """Provide an API client configured with the base URL"""
    return Client("https://http.cat/status")