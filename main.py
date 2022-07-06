import re
import pprint

class App:
    def __init__(self, apikey,apikey_secret, bearer_token):
        """
        Creates a new instance with the API key
        :param apikey:
        """
        self.apikey = apikey
        self.apikey_secret = apikey_secret
        self.bearer_token = bearer_token



    def start(self):
     """funcion utilizada para lanzar test"""
        print("funcion")
        


    def __str__(self):
        """
        Prints match_code when printing the object
        :return:
        """
        return str(self.start())


if __name__ == "__main__":
    # Runtime around 3/4 seconds per match
    app = App('SspqTw5jspgRdH2KLk3GmEMLn',
                'RsImEASvEx21sLD09lNoQAiyNVQtKxWu8gzdCV6qGvkGubt6I0',
                'AAAAAAAAAAAAAAAAAAAAAGEkegEAAAAAUTtrkarPpc6w0sPxGBpjCbYzMU0%3DR8Ma8gS9xDqeDaZ9BO05oqNh6aiCahZP8lS9MX2OI8CqsviC8E')
    print(app)
   # print(app.end_time - app.start_time)