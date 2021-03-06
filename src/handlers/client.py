from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from bot import bot
from config.languages import default_language as d_lan
from config.languages import languages
from services import film, user
from utils import keyboard as nav

data = {"name": None, "genre": None, "comments": None}
bot.state = None

NAME = 1
GENRE = 2
COMMENTS = 3
MARK = 4
data_list = []


async def start(message: types.Message):
    response = user.save_user(message=message)
    first_name = message.from_user.first_name

    if response["status_code"] == 200:
        await message.answer(
            f"{languages[d_lan]['hi']} {first_name}!\n{languages[d_lan]['welcome']}",
            reply_markup=nav.menu,
        )
    elif response["status_code"] == 409:
        await message.answer(
            f"{languages[d_lan]['comeback']} {first_name}!",
            reply_markup=nav.menu,
        )
    else:
        await message.answer(languages[d_lan]["error"])


async def get_all_films(message: types.Message):
    await film.retrieve_films(message)


async def get_all_reviewed_films(message: types.Message):
    await film.retrieve_reviewed_films(message)


async def get_all_unreviewed_films(message: types.Message):
    await film.retrieve_unreviewed_films(message)


async def add_film(message: types.Message):
    global data
    data = {"name": None, "genre": None, "comments": None}

    await bot.send_message(
        message.chat.id,
        f"{languages[d_lan]['note']}",
        reply_markup=nav.addMenu,
    )
    bot.state = NAME


async def add_tittle(message: types.Message):
    data["name"] = message.text

    await bot.send_message(
        message.chat.id,
        f"{languages[d_lan]['name']} {message.text}\n{languages[d_lan]['nowAddGenre']}",
    )
    bot.state = GENRE


async def add_genre(message: types.Message):
    data["genre"] = message.text

    await bot.send_message(
        message.chat.id,
        f"{languages[d_lan]['genre']} {message.text}\n{languages[d_lan]['nowAddComment']}",
    )
    bot.state = COMMENTS


async def add_comment(message: types.Message):
    data["comments"] = message.text

    await bot.send_message(message.chat.id, f"{languages[d_lan]['comment']} {message.text}")

    msg = f"""{languages[d_lan]['gotData']}
    {languages[d_lan]['name']} {data['name']}
    {languages[d_lan]['genre']} {data['genre']}
    {languages[d_lan]['comment']} {data['comments']}
    """
    await bot.send_message(message.chat.id, msg, reply_markup=nav.menu)
    bot.state = None
    await film.add_film(message, data)


async def cancel(message: types.Message):
    await message.answer(f"{languages[d_lan]['cancelAddingFilm']}", reply_markup=nav.menu)
    bot.state = None


async def delete(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id, text=f"{languages[d_lan]['wasDeleted']}")
    r = await film.delete(callback)
    if r == 200:
        await bot.edit_message_text(
            f"{languages[d_lan]['wasDeleted']}",
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
        )


async def review(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id, text=f"{languages[d_lan]['reviewed']}")
    await bot.send_message(
        chat_id=callback.message.chat.id,
        text=f"{languages[d_lan]['markFilm']}",
    )
    global data_list
    data_list.append(callback.from_user.id)
    data_list.append(callback.message.text)
    bot.state = MARK


async def add_mark(message: types.Message):
    mark = message.text
    r = await film.review(data_list, mark)
    if r == 200:
        await bot.send_message(message.chat.id, f"{languages[d_lan]['filmWasMarked']} {mark}")
    bot.state = None


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(add_film, Text(contains=f"{languages[d_lan]['addFilm']}"))
    dp.register_message_handler(get_all_films, Text(contains=f"{languages[d_lan]['allFilms']}"))
    dp.register_message_handler(
        get_all_reviewed_films,
        Text(contains=f"{languages[d_lan]['reviewedFilms']}"),
    )
    dp.register_message_handler(
        get_all_unreviewed_films,
        Text(contains=f"{languages[d_lan]['unreviewedFilms']}"),
    )
    dp.register_message_handler(cancel, Text(contains=f"{languages[d_lan]['cancel']}"))
    dp.register_message_handler(add_tittle, lambda msg: bot.state == NAME)
    dp.register_message_handler(add_genre, lambda msg: bot.state == GENRE)
    dp.register_message_handler(add_comment, lambda msg: bot.state == COMMENTS)
    dp.register_callback_query_handler(delete, lambda c: c.data == "delete")
    dp.register_callback_query_handler(review, lambda c: c.data == "reviewed")
    dp.register_message_handler(add_mark, lambda msg: bot.state == MARK)
