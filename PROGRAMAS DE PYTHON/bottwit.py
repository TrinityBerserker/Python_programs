import tweepy
import requests
from bs4 import BeautifulSoup
import time

# Credenciales de API de Twitter
API_KEY = 'tu_api_key'
API_SECRET_KEY = 'tu_api_secret_key'
ACCESS_TOKEN = 'tu_access_token'
ACCESS_TOKEN_SECRET = 'tu_access_token_secret'

# Autenticación en Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# URLs de RT Noticias y Sputnik
rt_url = 'https://www.rt.com/news/ukraine/'
sputnik_url = 'https://sputniknews.com/europe/'

# Función para obtener noticias
def get_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('h2')
    return [headline.get_text() for headline in headlines]

# Función para hacer tweets sarcásticos
def post_sarcastic_tweet():
    sarcastic_tweets = [
        "Just when you thought things couldn't get more complicated in Ukraine...",
        "Another day, another news from Ukraine. What's next?",
        "Ukraine update: Because clearly, we needed more drama in the world.",
        "Breaking news from Ukraine! Because regular news just isn't dramatic enough."
    ]
    tweet = random.choice(sarcastic_tweets)
    api.update_status(tweet)

# Función principal
def main():
    while True:
        # Obtener y publicar noticias de RT
        rt_news = get_news(rt_url)
        for news in rt_news[:3]:  # Limitar a 3 noticias para no exceder el límite de Twitter
            api.update_status(f"RT Noticias: {news} #Ukraine")
        
        # Obtener y publicar noticias de Sputnik
        sputnik_news = get_news(sputnik_url)
        for news in sputnik_news[:3]:
            api.update_status(f"Sputnik: {news} #Ukraine")
        
        # Publicar un tweet sarcástico
        post_sarcastic_tweet()
        
        # Esperar 10 minutos
        time.sleep(600)

if __name__ == "__main__":
    main()
