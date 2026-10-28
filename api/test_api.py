import pytest

from api.utils import parse_html_response


@pytest.mark.parametrize(
    "status_code, expected_h1, expected_title",
    [
        ("100", "100 Continue", "100 Continue | HTTP Cats"),
        ("200", "200 OK", "200 OK | HTTP Cats"),
        ("301", "301 Moved Permanently", "301 Moved Permanently | HTTP Cats"),
        ("404", "404 Not Found", "404 Not Found | HTTP Cats"),
        ("500", "500 Internal Server Error", "500 Internal Server Error | HTTP Cats"),
    ],
    ids=["1xx", "2xx", "3xx", "4xx", "5xx"],
)
def test_endpoint(api_client, status_code, expected_h1, expected_title):
    """Verify that https://http.cat/status/<code> returns a valid HTML page for each status group (1xx-5xx)"""
    get_response = api_client.get_request(status_code)

    assert get_response.status_code == 200
    assert "text/html" in get_response.headers["Content-Type"]
    assert parse_html_response(get_response.text, "main h1") == expected_h1
    assert parse_html_response(get_response.text, "title") == expected_title


def test_base_url_without_specifying_endpoint(api_client):
    """Verify that https://http.cat/status/ returns 404 status code"""
    get_response = api_client.get_request("")

    assert get_response.status_code == 404
    assert "image/jpeg" in get_response.headers["Content-Type"]
