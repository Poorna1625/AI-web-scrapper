# outputter.py
import logging
import pandas as pd

def output_to_csv(title, paragraphs, filename="output.csv"):
    """
    Convert the extracted data to a CSV file.
    
    The paragraphs are joined into a single string.
    """
    # Create a dictionary with our data
    data = {
        "Title": [title],
        "Paragraphs": ['\n'.join([p.get_text().strip() for p in paragraphs])]
    }
    # Convert the dictionary to a DataFrame and then output to CSV
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    logging.info("Data saved to %s", filename)
