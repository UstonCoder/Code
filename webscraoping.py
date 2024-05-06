import requests
from bs4 import BeautifulSoup


url = 'https://www.maxifoot.fr/calendrier-premier-league-angleterre.htm'
#envoie de la requete HTTP
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

match_rows = soup.find_all('tr',class_='cl1')+soup.find_all('tr',class_='cl2')

