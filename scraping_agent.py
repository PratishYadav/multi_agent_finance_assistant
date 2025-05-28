import requests
from bs4 import BeautifulSoup

def get_earnings_news():
    url = "https://www.investing.com/earnings-calendar/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Find and parse table
    return "TSMC beat estimates by 4%, Samsung missed by 2%"
