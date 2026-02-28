import os
import requests

api_key = os.getenv("API_KEY_TRANSLATE")
headers = {
    "Authorization": f"Api-Key {api_key}"
}

def get_translation(msg):
    data = {
        "folderId": "b1ge398im9j2peomr0me",
        "texts": [msg],
        "targetLanguageCode": "cv"
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate', headers=headers,json=data)

    return response
