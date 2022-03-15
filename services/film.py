import json
import requests

from config import settings
from serializers.film import film_serializer


async def retrieve_films(message):
    r = requests.get(url=f"{settings.get_films}{message.from_user.id}")
    films = r.text
    await film_serializer(films=json.loads(films), message=message)


async def retrieve_reviewed_films(message):
    url = settings.get_films
    user_id = message.from_user.id
    r = requests.get(
        url=f"{url}{user_id}?parameter=viewed&query=True"
    )
    films = r.text
    await film_serializer(films=json.loads(films), message=message)


async def retrieve_unreviewed_films(message):
    url = settings.get_films
    user_id = message.from_user.id
    r = requests.get(
        url=f"{url}{user_id}?parameter=viewed&query=False"
    )
    films = r.text
    await film_serializer(films=json.loads(films), message=message)
