from typing import List
from config.languages import languages
from config.languages import default_language as d_lan
from utils import keyboard as nav


async def film_serializer(films: List, message):
    if len(films) >= 1:
        count = 1
        for film in films:
            await message.answer(f"""
            {count}.<b>{languages[d_lan]['name']}</b> {film["name"]}
            <b>{languages[d_lan]['genre']}</b> {film["genre"]}
            <b>{languages[d_lan]['mark']}</b> {film["mark"]}
            <b>{languages[d_lan]['comment']}</b> {film["comments"]}
            """, parse_mode="html", reply_markup=nav.inlineMenu)
            count += 1
    else:
        await message.answer(
            f"{languages[d_lan]['noSavedFilms']}"
        )
