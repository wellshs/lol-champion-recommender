#-*-coding: utf-8-*-
from bs4 import BeautifulSoup
import json
import urllib.request
import urllib.parse
import numpy as np


champion_json = json.load(open('champion.json'))
champion_names = list(map(lambda x:x['name'], champion_json['data'].values()))
champion_names.sort()
champion_map = dict(map(lambda x: (x[1], x[0]), list(enumerate(champion_names))))

def name_to_index(champion_name):
    return champion_map[champion_name]

def extract_feature_from_name(name):
    data = {}
    url = 'http://www.op.gg/summoner/champions/userName=' + urllib.parse.quote_plus(name)

    feature = np.zeros((140, 15))
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        champ_list = soup.find('div', {'class':'season-11--all'}).find('tbody').find_all('tr', {'class':'Row'})

        for champ_row in champ_list:
            #find div for extraction
            champion_div = champ_row.find('td', {'class':'ChampionName'})
            win_lose_div = champ_row.find('div', {'class':'Graph'})
            kda_div = champ_row.find('div', {'class': 'KDA'})
            other_list = champ_row.find_all('td', {'class': 'Value Cell'})

            #extract feature from div
            champion_name = champion_div.find('a').text
            win = win_lose_div.find('div', {'class': 'Text Left'}).text.replace('W','') if win_lose_div.find('div', {'class': 'Text Left'}) else '0'
            lose = win_lose_div.find('div', {'class': 'Text Right'}).text.replace('L', '') if win_lose_div.find('div', {'class': 'Text Right'}) else '0'
            kill = kda_div.find('span', {'class': 'Kill'}).text
            death = kda_div.find('span', {'class': 'Death'}).text
            assist = kda_div.find('span', {'class': 'Assist'}).text
            other_features = list(map(lambda x:x if x!='' else '0', map(lambda x:x.text.strip(), other_list)))

            #make final feature shape
            feature_list = [win, lose, kill, death, assist]
            feature_list.extend(other_features)
            feature_list = list(map(lambda x:float(x), map(lambda x:x.replace(",",""), feature_list)))

            #make feature to np array
            idx = name_to_index(champion_name)
            feature[idx] = feature_list

    return feature

if __name__=="__main__":
    print(extract_feature_from_name("KSV 코어장전"))
