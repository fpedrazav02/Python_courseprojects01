
import requests
import pprint
from bs4 import BeautifulSoup


def ft_sorted(hn_list):
    return sorted(hn_list, key=lambda k: k['Votes'], reverse=True)


def ft_display_hn(links, subtext):
    hn_list = []

    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        score_tag = subtext[index].select('.score')
        if len(score_tag):
            upvotes = int(score_tag[0].getText().replace(' points', ''))
            if upvotes >= 150:
                hn_list.append(
                    {'title': title, 'link': href, 'Votes': upvotes})
    return hn_list


if __name__ == '__main__':
    daily_news = []
    for indexp in range(1, 10):
        req = requests.get(f'https://news.ycombinator.com/news?p={indexp}')
        soup = BeautifulSoup(req.text, 'html.parser')

        links = soup.select('.titlelink')
        subtext = soup.select('.subtext')
        daily_news = ft_display_hn(links, subtext)
    pprint.pprint(ft_sorted(daily_news))
