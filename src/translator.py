import requests
import os
import uuid
import json


class Translator:
    def __init__(self):
        self.api_key = os.getenv("MICROSOFT_TRANSLATOR")
        self.location = os.getenv("MICROSOFT_LOCATION")
        self.endpoint = "https://api.cognitive.microsofttranslator.com"

    def translate(self, text):
        path = '/translate'
        constructed_url = self.endpoint + path

        params = {
            'api-version': '3.0',
            'to': 'en'
        }

        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key,
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': text
        }]

        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()

        text = response[0]["translations"][0]["text"]

        return text
