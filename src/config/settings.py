import os

TOKEN = os.getenv("TOKEN", "")
headers = {"accept": "application/json", "Content-Type": "application/json"}
users_url = "http://172.28.0.4:8000/users/"
films_url = "http://172.28.0.4:8000/films/"
