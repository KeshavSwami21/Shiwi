from skills import factory
from dataclasses import dataclass
from ai import AI
import requests
from bs4 import BeautifulSoup

shiwi = AI()
# shiwi.say("Hello") #Checked the ai import
url = "https://www.bbc.com/news"
response = requests.get(url)

@dataclass
class News_skill:
    name = "news_skill"
    
    def commands(self, command:str):
        return ['news', 'tell me news', 'what is the news', 'what\'s the news', 'what\'s on the headline', 'headlines'\
            'tell me today\'s news', 'today\'s news']
   
    def handle_command(self, command:str, ai:AI):
    
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find('body').find_all('h3')

        for x in headlines:
            shiwi.say(x.text.strip())

def initialize():
    factory.register("news_skill", News_skill)
