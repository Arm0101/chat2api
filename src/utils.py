import requests
from bs4 import BeautifulSoup

def load_content(url):
    if not url.startswith(("http://", "https://")):
        raise ValueError("La URL debe comenzar con http:// o https://")
    
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    text = soup.get_text()

    return text
    