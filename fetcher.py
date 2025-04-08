# fetcher.py
import logging
import requests
from playwright.sync_api import sync_playwright
from tenacity import retry, wait_fixed, stop_after_attempt

# Custom headers for requests
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/116.0.5845.188 Safari/537.36"
    )
}

@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
def fetch_static(url):
    """
    Fetch the webpage using requests (static method) and return the HTML content.
    """
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()  # Raises an exception for HTTP errors.
    return response.text

def fetch_dynamic(url):
    """
    Fetch the webpage using Playwright (dynamic method) to capture JavaScript-rendered content.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, wait_until='networkidle', timeout=15000)
            html = page.content()
        except Exception as e:
            logging.error("Error using Playwright: %s", e)
            html = None
        finally:
            browser.close()
    return html
