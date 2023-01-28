from config import dp, bot
from aiogram import types
total = 150

@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}! '
                                                     'Сыграем в игру? На столе лежат вкусные конфетки "Baunty - Райское наслаждение."'
                                                     'Количество конфет 150. '
                                                     'Немного о правилах игры, делаем ход друг после друга. Первый ход определяется жеребьёвкой.'
                                                     'За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему'
                                                     'последний ход. Если согласен жми на /game')
@dp.message_handler(commands='game')
async def game_bot(message: types.Message):
    await message.answer(f'Твой ход! Введи сколько хочешь взять конфет.')

@dp.message_handler()
async def all_bot(message: types.Message):
    print(message.text)
    global total
    take = int(message.text)
    if total==0:
        await message.answer(f'Game over')
    elif 0 < take < 29:
        total -= int(message.text)
        bbb = total - ((total // 29) * 29)
        await message.reply(f'{message.from_user.first_name},ты взял(а) {message.text} конфет и на столе осталось {total}')
        total -= bbb
        await bot.send_message(message.from_user.id, f'я беру {bbb} и на столе осталось {total}')


    else:
        await message.reply(f'{message.from_user.first_name}, не жульничай')
        await bot.send_message(message.from_user.id, f'Давай еще раз', )


