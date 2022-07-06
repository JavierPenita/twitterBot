import datetime
import logging as logger
import time 
import os.path
import tweepy
import schedule
import credentials
from tweepy.auth import OAuthHandler

class App:
    def __init__(self):
        """
        Creates a new instance with the API key
        :param apikey:
        """
        #self.auth = tweepy.AppAuthHandler(credentials.API_key, credentials.API_secret_key)
        #self.auth.set_access_token(credentials.access_token,credentials.access_token_secret)
        self.auth = OAuthHandler(credentials.API_key, credentials.API_secret_key)
        self.auth.set_access_token(credentials.access_token, credentials.access_token_secret)
        self.api = tweepy.API(self.auth)
        
    def logger(self, logtext):
        logger.debug(str(datetime.datetime.now()) + " | " + logtext)
        print(str(datetime.datetime.now()) + " | " + logtext)

    def job(self):
        self.logger("Estado")
        #Definiremos la variable como global
        global lastTweet_ID
        lastTweet_ID = 0
        # Leer lineas del archivo
        file = open("tweets.txt", "r")
        tweets = file.readlines()
        self.logger(str(tweets))
        self.logger("ID:" + str(lastTweet_ID) + "   Texto: " + tweets[lastTweet_ID])
        # Publicar estado
        self.api.update_status(tweets[lastTweet_ID])
        # Actualizar variable ID con la del nuevo tweet
        lastTweet_ID = lastTweet_ID + 1;
        # Comprobar que no hemos sobrepasado el limite de publicaciones
        if lastTweet_ID >= len(tweets):
            lastTweet_ID = 0
        self.logger("Updated status.")
        # Abrir config y guardar ID de este tweet
        file = open("config.txt", "w+")
        file.writelines(str(lastTweet_ID))
        file.close()

    def start(self):
        """funcion utilizada para lanzar test"""
        try:
            self.api.auth
            self.logger("Authentication Successful")
        except:
            self.logger("Authentication Error")
        self.job()
        # Programar cada 60 segundos
        schedule.every(60).seconds.do(self.job)
        while True:
            schedule.run_pending()
            time.sleep(1)
                

    def __str__(self):
        """
        Prints match_code when printing the object
        :return:
        """
        return str(self.start())


if __name__ == "__main__":
    # Runtime around 3/4 seconds per match
    app = App()
    print(app)
   # print(app.end_time - app.start_time)