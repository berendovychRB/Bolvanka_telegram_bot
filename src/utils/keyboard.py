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
addMenu = ReplyKeyboardMarkup(resize_keyboard=True)
addMenu.row(btnCancel)


'''***************************** InlineMenu ****************************'''
btnDelete = InlineKeyboardButton(f"{languages[d_lan]['delete']}",
                                 callback_data="delete")
btnReviewed = InlineKeyboardButton(f"{languages[d_lan]['reviewed']}",
                                   callback_data="reviewed")
inlineMenu = InlineKeyboardMarkup().add(btnDelete, btnReviewed)
inlineMenuWithoutReview = InlineKeyboardMarkup().add(btnDelete)
