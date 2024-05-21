from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config
import logging
from lyrics import *
from translated_texts import *
from history_song import *
import keyboards

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(message)s",
)

storage = MemoryStorage()
bot = Bot(token=config.token, parse_mode='HTML')
dp = Dispatcher(bot, storage = storage)


@dp.message_handler(commands=['start'])
async def start(message:types.message):
    reply = 'Привет, дорогой друг. \n' \
                'Этот бот поможет тебе узнать больше о шведской группе Sabaton.\n\n' \
                'Напиши /help, чтобы узнать мои функции'
    await message.answer(reply)

@dp.message_handler(commands=['help'])
async def help(message: types.message):
    reply_help = 'Чем могу помочь?'
    await message.reply(
        text=reply_help,
        reply=False,
        reply_markup=await keyboards.help(),
        disable_web_page_preview=True)

#lyrics

@dp.callback_query_handler(text='song')
async def song(call: types.callback_query):
    '''Обработка вывода списка песен'''
    reply_help = 'Выберите песню'
    await call.message.reply(
        text=reply_help,
        reply=False,
        reply_markup=await keyboards.songs(),
        disable_web_page_preview=True)
    await call.answer()

@dp.callback_query_handler(text='song1')
async def song1(call: types.callback_query):
    """Обработка вывода текста 1 песни"""
    await call.message.answer(ToHell)
    await call.answer()

@dp.callback_query_handler(text='song2')
async def song1(call: types.callback_query):
    """Обработка вывода текста 2 песни"""
    await call.message.answer(NightWitches)
    await call.answer()

@dp.callback_query_handler(text='song3')
async def song1(call: types.callback_query):
    """Обработка вывода текста 3 песни"""
    await call.message.answer(DeadMen)
    await call.answer()

@dp.callback_query_handler(text='song4')
async def song1(call: types.callback_query):
    """Обработка вывода текста 4 песни"""
    await call.message.answer(Panzer)
    await call.answer()

@dp.callback_query_handler(text='song5')
async def song1(call: types.callback_query):
    """Обработка вывода текста 5 песни"""
    await call.message.answer(Bismark)
    await call.answer()

@dp.callback_query_handler(text='song6')
async def song1(call: types.callback_query):
    """Обработка вывода текста 6 песни"""
    await call.message.answer(Verdun)
    await call.answer()

@dp.callback_query_handler(text='song7')
async def song1(call: types.callback_query):
    """Обработка вывода текста 7 песни"""
    await call.message.answer(DefMoscow)
    await call.answer()

#translate

@dp.callback_query_handler(text='translate')
async def song(call: types.callback_query):
    '''Обработка вывода списка песен'''
    reply_help = 'Выберите песню'
    await call.message.reply(
        text=reply_help,
        reply=False,
        reply_markup=await keyboards.translates(),
        disable_web_page_preview=True)
    await call.answer()

@dp.callback_query_handler(text='translate1')
async def song1(call: types.callback_query):
    await call.message.answer(ToHell_trans)
    await call.answer()

@dp.callback_query_handler(text='translate2')
async def song1(call: types.callback_query):
    await call.message.answer(NightWitches_trans)
    await call.answer()

@dp.callback_query_handler(text='translate3')
async def song1(call: types.callback_query):
    await call.message.answer(DeadMen_trans)
    await call.answer()

@dp.callback_query_handler(text='translate4')
async def song1(call: types.callback_query):
    await call.message.answer(Panzer_trans)
    await call.answer()

@dp.callback_query_handler(text='translate5')
async def song1(call: types.callback_query):
    await call.message.answer(Bismark_trans)
    await call.answer()

@dp.callback_query_handler(text='translate6')
async def song1(call: types.callback_query):
    await call.message.answer(Verdun_trans)
    await call.answer()

@dp.callback_query_handler(text='translate7')
async def song1(call: types.callback_query):
    await call.message.answer(DefMoscow_trans)
    await call.answer()

#history

@dp.callback_query_handler(text='history')
async def song(call: types.callback_query):
    '''Обработка вывода списка песен'''
    reply_help = 'Выберите песню'
    await call.message.reply(
        text=reply_help,
        reply=False,
        reply_markup=await keyboards.histories(),
        disable_web_page_preview=True)
    await call.answer()

@dp.callback_query_handler(text='history1')
async def song1(call: types.callback_query):
    await call.message.answer(ToHell_history)
    await call.answer()

@dp.callback_query_handler(text='history2')
async def song1(call: types.callback_query):
    await call.message.answer(NightWitches_history)
    await call.answer()

@dp.callback_query_handler(text='history3')
async def song1(call: types.callback_query):
    await call.message.answer(DeadMen_history)
    await call.answer()

@dp.callback_query_handler(text='history4')
async def song1(call: types.callback_query):
    await call.message.answer(Panzer_history)
    await call.answer()

@dp.callback_query_handler(text='history5')
async def song1(call: types.callback_query):
    await call.message.answer(Bismark_history)
    await call.answer()

@dp.callback_query_handler(text='history6')
async def song1(call: types.callback_query):
    await call.message.answer(Verdun_history)
    await call.answer()

@dp.callback_query_handler(text='history7')
async def song1(call: types.callback_query):
    await call.message.answer(DefMoscow_history)
    await call.answer()

if __name__ == "__main__":
    logger.info("Starting bot")
    executor.start_polling(dp, skip_updates=True)
