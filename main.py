import requests
import bs4
import re
from fake_user_agent import fake_user_agent

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
PATTERN = r'(\W|^)(дизайн|фото|web|python)(\W|$)'

url_all = 'https://habr.com/ru/all'
url_habr = 'https://habr.com'


if __name__ == '__main__':
    regular = re.compile(PATTERN, flags=re.I)

    response = requests.get(url_all, headers=fake_user_agent)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    articals = soup.find_all('article')
    for artical in articals:
        result = []
        previev = artical.find(class_='article-formatted-body')
        if regular.search(previev.text):
            date = artical.find(class_='tm-article-snippet__datetime-published').text
            hed = artical.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find('span').text
            link = artical.h2.a.get('href')
            print(f"""Дата публикации - {date}
                      \rЗаголовок статьи - {hed}
                      \rСсылка - {url_habr}{link}\n""")



