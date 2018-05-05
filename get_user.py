#-*-coding: utf-8-*-
from bs4 import BeautifulSoup
import urllib.request

def get_user_from_url(url):
    user_list = []
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        tds = soup.find_all('td', {'class': 'ranking-table__cell--summoner'})
        for td in tds:
            summoner_name = td.find('span').text
            user_list.append(summoner_name)
    return user_list

def get_user_list(start=1, end=22900, step=200):
    base_url = "http://www.op.gg/ranking/ladder/page={}"
    user_list = ['GabrielCRO', 'DWG ShowMaker', 'yizhiyu', 'MVP ADD', 'SKT T1 Bang']
    for page_num in range(start, end, step):
        url = base_url.format(page_num)
        user_list.extend(get_user_from_url(url))
    return user_list

if __name__ == "__main__":
    user_list = get_user_list()
    f = open("user_list.txt", "w")
    for user in user_list:
        f.write(user +'\n')
    f.close()
