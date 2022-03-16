import json
import logging

import requests

from config import settings
from serializers.film import film_serializer


async def retrieve_films(message):
    r = requests.get(url=f"{settings.films_url}{message.from_user.id}")
    films = r.text
    await film_serializer(films=json.loads(films), message=message)


async def retrieve_reviewed_films(message):
    url = settings.films_url
    user_id = message.from_user.id
    r = requests.get(
        url=f"{url}{user_id}?parameter=viewed&query=True"
    )
    films = r.text
    await film_serializer(films=json.loads(films), message=message)


async def retrieve_unreviewed_films(message):
    url = settings.films_url
    user_id = message.from_user.id
    r = requests.get(
        url=f"{url}{user_id}?parameter=viewed&query=False"
    )
    films = r.text
    await film_serializer(films=json.loads(films), message=message)


async def add_film(message, data):
    url = settings.films_url
    user_id = message.from_user.id
    data["user_id"] = user_id
    r = requests.post(
        url=url,
        headers=settings.headers,
        data=json.dumps(data)
    )
    logging.info(f"{r.status_code}|{r.text}")

