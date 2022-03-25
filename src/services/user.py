import json
import logging
import requests

from config import settings


def save_user(message):
    data = {
        "telegram_id": message.from_user.id,
        "username": message.from_user.username,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
    }

    r = requests.post(url=settings.users_url,
                      data=json.dumps(data),
                      headers=settings.headers)
    response = {
        "status_code": r.status_code,
        "text": r.content
    }
    logging.info(f"{response['status_code']}|{response['text']}")
    return response
