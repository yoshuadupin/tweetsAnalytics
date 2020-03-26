from twitterscraper import query_tweets
from twitterscraper import query_tweets_from_user
from ekphrasis.classes.segmenter import Segmenter
import re

#Se usaron dos librerias twitterscraper que es para hacer scraping de twitter y 
# ekphrasis que es para hacer sentimental analysis en especifico aqui se uso para la segmentacion de hashtags

#Metodo para limpiar tweets quitar caracteres especiales, hashtags y url
def clean_tweet( tweet): 
        tweet = re.sub(r"pic.\S+", "", tweet)
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", 
        " ", tweet).split()) 

#Query para los 20 tweets recientes
tweets = query_tweets_from_user("realDonaldTrump" ,20)

#Imprimir los tweets limpios
for tweet in tweets:
    print(clean_tweet(tweet.text))
    tweetHashtag = re.findall(r"#(\w+)", tweet.text)
    if tweetHashtag.__len__ != 0:
        hashtagArray.extend(tweetHashtag)
    print("\n")

#El corpus se refiere a las estadisticas que usara para segmentar los hashtags en este caso son de twitter
seg_tw = Segmenter(corpus="twitter")
hashtagArray = []  

print("Hashtags Segmention:\n")

for hashtag in hashtagArray:#
       print("(tw):", seg_tw.segment(hashtag))

