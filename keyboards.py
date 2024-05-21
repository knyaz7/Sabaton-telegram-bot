from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

async def help():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(
            text='Текст песни',
            callback_data = 'song'
        ),
        InlineKeyboardButton(
            text='Перевод песни',
            callback_data = 'translate'
        ),
        InlineKeyboardButton(
            text='История песни',
            callback_data = 'history'
        ))
    return markup

async def songs():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(
            text='To Hell And Back',
            callback_data='song1'
        ),
        InlineKeyboardButton(
            text='Night Witches',
            callback_data='song2'
        ),
        InlineKeyboardButton(
            text='The Attack of the Dead Men',
            callback_data='song3'
        ),
        InlineKeyboardButton(
            text='Panzerkampf',
            callback_data='song4'
        ),
        InlineKeyboardButton(
            text='Bismark',
            callback_data='song5'
        ),
        InlineKeyboardButton(
            text='Fields of Verdun',
            callback_data='song6'
        ),
        InlineKeyboardButton(
            text='Defence of Moscow',
            callback_data='song7'
        )
    )
    return markup

async def translates():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(
            text='To Hell And Back',
            callback_data='translate1'
        ),
        InlineKeyboardButton(
            text='Night Witches',
            callback_data='translate2'
        ),
        InlineKeyboardButton(
            text='The Attack of the Dead Men',
            callback_data='translate3'
        ),
        InlineKeyboardButton(
            text='Panzerkampf',
            callback_data='translate4'
        ),
        InlineKeyboardButton(
            text='Bismark',
            callback_data='translate5'
        ),
        InlineKeyboardButton(
            text='Fields of Verdun',
            callback_data='translate6'
        ),
        InlineKeyboardButton(
            text='Defence of Moscow',
            callback_data='translate7'
        )
    )
    return markup

async def histories():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(
            text='To Hell And Back',
            callback_data='history1'
        ),
        InlineKeyboardButton(
            text='Night Witches',
            callback_data='history2'
        ),
        InlineKeyboardButton(
            text='The Attack of the Dead Men',
            callback_data='history3'
        ),
        InlineKeyboardButton(
            text='Panzerkampf',
            callback_data='history4'
        ),
        InlineKeyboardButton(
            text='Bismark',
            callback_data='history5'
        ),
        InlineKeyboardButton(
            text='Fields of Verdun',
            callback_data='history6'
        ),
        InlineKeyboardButton(
            text='Defence of Moscow',
            callback_data='history7'
        )
    )
    return markup