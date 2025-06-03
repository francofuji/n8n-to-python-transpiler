from bs4 import BeautifulSoup
from jinja2 import Template
import pandas as pd
from typing import List, Dict, Any

def extract_html_content(html: str, selectors: Dict[str, str], return_values: str = "text") -> List[Dict[str, Any]]:
    """
    Extracts content from HTML using CSS selectors.

    :param html: The HTML content as a string.
    :param selectors: A dictionary mapping keys to CSS selectors.
    :param return_values: 'text' or 'html' to specify the return format.
    :return: A list of dictionaries with extracted content.
    """
    soup = BeautifulSoup(html, 'html.parser')
    results = []

    # Find all elements matching the first selector to determine the number of items
    first_selector = next(iter(selectors.values()))
    elements = soup.select(first_selector)

    for i in range(len(elements)):
        item = {}
        for key, selector in selectors.items():
            selected_elements = soup.select(selector)
            if i < len(selected_elements):
                element = selected_elements[i]
                item[key] = element.get_text(strip=True) if return_values == "text" else str(element)
            else:
                item[key] = None
        results.append(item)

    return results

def generate_html_template(template_str: str, data: Dict[str, Any]) -> str:
    """
    Generates HTML content from a template string and data.

    :param template_str: The HTML template as a string.
    :param data: A dictionary of data to populate the template.
    :return: The rendered HTML content.
    """
    template = Template(template_str)
    return template.render(**data)

def convert_to_html_table(data: List[Dict[str, Any]]) -> str:
    """
    Converts a list of dictionaries to an HTML table.

    :param data: A list of dictionaries representing rows.
    :return: An HTML string representing the table.
    """
    df = pd.DataFrame(data)
    return df.to_html(index=False, escape=False)
