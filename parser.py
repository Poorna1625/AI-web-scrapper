# parser.py
from bs4 import BeautifulSoup

def parse_html(html):
    """
    Parse HTML with BeautifulSoup and extract title and paragraphs.
    
    Returns:
        title (str): The page title.
        paragraphs (list): A list of BeautifulSoup paragraph objects.
    """
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string.strip() if soup.title else "No title found"
    paragraphs = soup.find_all('p')
    return title, paragraphs
