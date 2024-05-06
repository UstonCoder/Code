import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.maxifoot.fr/calendrier-premier-league-angleterre.htm'
#envoie de la requete HTTP
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

match_rows = soup.find_all('tr', class_='cl1')+soup.find_all('tr', class_='cl2')

matches = []
for match in match_rows:
    teams = match.find_all('a',class_='eqc')
    score = match.find('th').text.strip()

    if teams and len(teams) == 2:
        home_team = teams[0].text
        away_team = teams[1].text
        try :
            home_goals, away_goals =map(int,score.split('-'))
            matches.append([home_team, home_goals, away_goals, away_team])
        except ValueError:
            print('Invalid')


df = pd.DataFrame(matches,columns=['home_team','home_goals','away_goals','away_team'])
