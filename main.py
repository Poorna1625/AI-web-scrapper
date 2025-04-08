# main.py
import logging
from fetcher import fetch_static, fetch_dynamic
from parser import parse_html
from outputter import output_to_csv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main(url):
    # First, try static scraping
    try:
        html = fetch_static(url)
        logging.info("Static content fetched successfully.")
    except Exception as e:
        logging.warning("Static fetch failed: %s. Trying dynamic fetch...", e)
        html = fetch_dynamic(url)
    
    if not html:
        logging.error("Failed to retrieve page content from both static and dynamic methods.")
        return

    # Parse the HTML content
    title, paragraphs = parse_html(html)
    logging.info("Title: %s", title)
    for idx, paragraph in enumerate(paragraphs, 1):
        logging.info("Paragraph %d: %s", idx, paragraph.get_text().strip())

    # Output the result to a CSV file
    output_to_csv(title, paragraphs)

if __name__ == "__main__":
    # Define the URL to scrape; change this to test different pages
    url = "https://example.com"
    main(url)
