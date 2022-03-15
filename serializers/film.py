from typing import List


async def film_serializer(films: List, message):
    if len(films) >= 1:
        count = 1
        for film in films:
            await message.answer(f"""
            {count}.<b>Name:</b> {film["name"]}
            <b>Genre:</b> {film["genre"]}
            <b>Mark:</b> {film["mark"]}
            <b>Comment:</b> {film["comments"]}
            """, parse_mode="html")
            count += 1
    else:
        await message.answer(
            "You haven't saved any movies yet"
        )
