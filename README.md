# Web Scraper with Dynamic Content Handling

A robust Python web scraper that combines static scraping using `requests` with dynamic content handling via `Playwright`. The scraper extracts key elements (e.g., page titles and paragraphs) from webpages and outputs the data as a CSV file. The project is designed with a modular architecture to ensure ease of maintenance, testing, and future enhancements.

## Features

- **Static and Dynamic Fetching**
  - **Static Fetching:** Uses `requests` with custom headers and retry logic (via `tenacity`) to fetch HTML content from websites.
  - **Dynamic Fetching:** Uses `Playwright` to render pages with JavaScript and retrieve the fully rendered HTML.
- **HTML Parsing**
  - Utilizes `BeautifulSoup` to parse HTML and extract useful data such as page titles and paragraphs.
- **Data Output**
  - Structures the extracted data and saves it as a CSV file using `pandas`.
- **Robust Error Handling & Logging**
  - Integrated error handling and logging to assist with debugging and ensure reliability.
- **Modular Code Structure**
  - The project is split into separate modules (`fetcher.py`, `parser.py`, `outputter.py`, and `main.py`) for easy management and extension.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment management (e.g., `venv`)

Project Structure
graphql
Copy
web-scrapper/
├── fetcher.py         # Handles static and dynamic fetching of web pages
├── parser.py          # Parses HTML content to extract titles and paragraphs
├── outputter.py       # Outputs the scraped data into CSV format using pandas
├── main.py            # Orchestrates the overall workflow
├── requirements.txt   # Lists project dependencies
└── README.md          # Project documentation (this file)

Run the scraper by executing the main.py script:
python main.py

