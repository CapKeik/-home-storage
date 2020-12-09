#source venv/bin/activate
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def process_start_and_first_instruction_command(msg: types.Message):
    await msg.answer(
        "Бот для учёта финансов\n\n"
        "Добавить расход: пример, '250 такси'\n"
        "Сегодняшняя статистика: /today\n"
        "За текущий месяц: /month\n"
        "За текущую неделю: /week"
        "Последние внесённые расходы: /expenses\n"
        "Категории трат: /categories")


@dp.message_handler(command=['categories'])
async def categories_list(message: types.Message):
    """Send categories"""
    categories = Categories().get_all_categories()

if __name__ == '__main__':
    executor.start_polling(dp)
