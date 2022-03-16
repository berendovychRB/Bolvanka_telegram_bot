from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)
from config.languages import default_language as d_lan
from config.languages import languages

'''**************************** Film Menu *****************************'''

btnAllFilms = KeyboardButton(f"{languages[d_lan]['allFilms']}")
btnReviewedFilms = KeyboardButton(f"{languages[d_lan]['reviewedFilms']}")
btnUnreviewedFilms = KeyboardButton(f"{languages[d_lan]['unreviewedFilms']}")
btnAddFilm = KeyboardButton(f"{languages[d_lan]['addFilm']}")
menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAllFilms,
                                                     btnReviewedFilms,
                                                     btnUnreviewedFilms,
                                                     btnAddFilm)

'''***************************** Add Menu *****************************'''

btnAddTittle = KeyboardButton(f"{languages[d_lan]['addTittle']}")
btnAddGenre = KeyboardButton(f"{languages[d_lan]['addGenre']}")
btnAddComment = KeyboardButton(f"{languages[d_lan]['addComment']}")
btnCancel = KeyboardButton(f"{languages[d_lan]['cancel']}")
btnConfirm = KeyboardButton(f"{languages[d_lan]['confirm']}")
addMenu = ReplyKeyboardMarkup(resize_keyboard=True)
addMenu.row(btnAddTittle, btnAddGenre, btnAddComment)
addMenu.row(btnCancel, btnConfirm)