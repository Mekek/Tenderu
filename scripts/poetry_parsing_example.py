import requests
from bs4 import BeautifulSoup

def parse_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Пример парсинга заголовков страницы
        headers = soup.find_all('h2')
        for header in headers:
            print(header.text.strip())
    else:
        print(f"Ошибка при получении страницы: {response.status_code}")

if __name__ == "__main__":
    website_url = "https://example.com"
    parse_website(website_url)



# Этот код отправляет GET-запрос к веб-сайту https://example.com,
# затем использует BeautifulSoup для разбора HTML-кода страницы и находит все заголовки второго уровня (<h2>). 
# Затем он выводит текст каждого заголовка на экран.