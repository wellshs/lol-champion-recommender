#-*-coding: utf-8-*-
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

data = {}

# 여러 개의 name에 대해서 opgg.py를 for문 돌면됨
name = 'hideonbush'
url = 'http://www.op.gg/summoner/champions/userName=' + urllib.parse.quote_plus(name)

data[name] = []

with urllib.request.urlopen(url) as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    champ_list = soup.find('div', {'class': 'season-11--all'}).find('tbody').find_all('td', {'class': 'ChampionName Cell'})
    win_lose_list = soup.find_all('div', {'class': 'Graph'})
    kda_list = soup.find_all('div', {'class': 'KDA'})
    others_list = soup.find_all('td', {'class': 'Value Cell'})

    for i in range(len(champ_list)):
      champ = str(champ_list[i]).split('>')[2].split('<')[0]

      win = win_lose_list[i].find('div', {'class': 'Text Left'})
      win = str(win).split('>')[1].split('<')[0][:-1] if win else '0'

      lose = win_lose_list[i].find('div', {'class': 'Text Right'})
      lose = str(lose).split('>')[1].split('<')[0][:-1] if lose else '0'

      kill = kda_list[i].find('span', {'class': 'Kill'})
      kill = str(kill).split('>')[1].split('<')[0]
      
      death = kda_list[i].find('span', {'class': 'Death'})
      death = str(death).split('>')[1].split('<')[0]

      assist = kda_list[i].find('span', {'class': 'Assist'})
      assist = str(assist).split('>')[1].split('<')[0]

      for j in range(10):
        idx = 10*i + j
        if j==0:
          gold = str(others_list[idx]).split('>')[1].split('<')[0].strip()
        elif j==1:
          cs = str(others_list[idx]).split('>')[1].split('<')[0].strip()
        elif j==2:
          destoyed_turret = str(others_list[idx]).split('>')[1].split('<')[0].strip()
        elif j==3:
          max_kill = str(others_list[idx]).split('>')[1].split('<')[0].strip()
        elif j==4:
          max_death = str(others_list[idx]).split('>')[1].split('<')[0].strip()
        elif j==5:
          gived_damage = str(others_list[idx]).split('>')[1].split('<')[0].strip()
        elif j==6:
          received_damage = str(others_list[idx]).split('>')[1].split('<')[0].strip()
        elif j==7:
          double_kill_cnt = str(others_list[idx]).split('>')[1].split('<')[0].strip()
          if double_kill_cnt == '':
            double_kill_cnt = '0'
        elif j==8:
          triple_kill_cnt = str(others_list[idx]).split('>')[1].split('<')[0].strip()
          if triple_kill_cnt == '':
            triple_kill_cnt = '0' 
        elif j==9:
          quadra_kill_cnt = str(others_list[idx]).split('>')[1].split('<')[0].strip()
          if quadra_kill_cnt == '':
            quadra_kill_cnt = '0' 

      data[name].append([champ, win, lose, kill, death, assist, gold, cs, destoyed_turret, max_kill, max_death, gived_damage, received_damage, double_kill_cnt, triple_kill_cnt, quadra_kill_cnt])

for d in data[name]:
  print(d)
#print(data[name])