import os
import dotenv
import requests


class GifSearcher:
    def __init__(self, limit=10, offset=0):
        self.limit = limit
        self.offset = offset
        self.tenor_key = os.getenv('TENOR_KEY')
        self.giphy_key = os.getenv('GIPHY_KEY')

    def __get_tenor(self, query):
        tenor_url = "https://api.tenor.com/v1/search"
        tenor_params = {
            "q": query,
            "key": self.tenor_key,
            "limit": 10,
            "pos": "0",
            "contentfilter": "high",
            "media_filter": "minimal",
            "ar_range": "all",
            "locale": "en_US",
        }
        tenor_response = requests.get(tenor_url, params=tenor_params)
        tenor_results = tenor_response.json()["results"]

        return tenor_results

    def __get_giphy(self, query):
        giphy_url = "https://api.giphy.com/v1/gifs/search"
        giphy_params = {
            "api_key": self.giphy_key,
            "q": query,
            "limit": 10,
            "offset": 0,
            "rating": "G",
            "lang": "en",
        }

        giphy_response = requests.get(giphy_url, params=giphy_params)
        giphy_results = giphy_response.json()["data"]

        return giphy_results

    def search_gif(self, keywords) -> str:
        query = " ".join(keywords)

        # Search for GIFs using the Giphy API
        giphy_results = self.__get_giphy(query)
        tenor_results = self.__get_tenor(query)

        # Find the GIFs that contain the most keywords
        max_keywords = 0
        best_gif = None
        for gif in giphy_results + tenor_results:
            num_keywords = len(set(keywords) & set(gif["title"].split()))
            if num_keywords > max_keywords:
                max_keywords = num_keywords
                best_gif = gif

        if best_gif is None:
            best_gif = self.__get_tenor(keywords[0])

            if best_gif is None:
                best_gif = self.__get_giphy(keywords[0])

        cleaned = ""

        if "tenor" in str(best_gif):
            cleaned = best_gif[0]['url']
        elif "giphy" in str(best_gif):
            cleaned = best_gif["url"]

        if not cleaned:
            cleaned = "https://tenor.com/bVh6d.gif"

        return cleaned
