from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    page_url = "https://economictimes.indiatimes.com/"
    #Access the HTML content from the webpage
    r = requests.get(page_url)

    #Parse the HTML Content using Beautifulsoup
    soup = BeautifulSoup(r.text, 'html.parser')
    h3_news = soup.find_all('h3')
    for item in h3_news:
        print(item.text)