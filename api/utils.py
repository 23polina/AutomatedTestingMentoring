from bs4 import BeautifulSoup


def parse_html_response(html_response: str, selector:str)-> str:
    """Return the text of the first HTML element that matches a CSS selector"""
    soup = BeautifulSoup(html_response, "html.parser")
    element = soup.select_one(selector)
    if not element:
        raise ValueError(f"Element {element} not found")
    return element.get_text(separator=" ", strip=True)
