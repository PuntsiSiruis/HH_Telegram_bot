from aiogram import Bot, types
from aiogram.dispatcher.filters import state

import butnn
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
class filtersforproject(StatesGroup):
    hp_job = State()
    tch_job = State()
    same = State()

bot = Bot(token='1969692948:AAED4IUekHGSxeLcdvNBMyc552FUtEeQF3s')

dp = Dispatcher(bot, storage=MemoryStorage())
print('РАБОТА ИДЁТ СТАБИЛЬНО')

@dp.message_handler(content_types=['text'])
async def main(message: types.Message):
    if message.text == 'привет' or message.text == '/старт' or message.text == '/start' or message.text == 'начать' or message.text == '/заново' or message.text == 'Привет' or message.text == 'Начать':
        await bot.send_message(message.from_user.id, f'Здравствуй!\nПриятно познакомится, {message.chat.first_name} {message.chat.last_name}')
        await bot.send_message(message.from_user.id, '😀', reply_markup=butnn.greet_kb)
    elif message.text == 'Выбрать вакансию':
        await bot.send_message(message.from_user.id, 'Выберите интересующий вас раздел 👉', reply_markup=butnn.vakan_kb)
    elif message.text == 'Безопасность':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()
        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)
        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data), reply_markup=butnn.hh_kb)
#await state.finish() в конце фильтров прописать
    elif message.text == 'Автомобильный бизнес':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()
        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)
        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data), reply_markup=butnn.hh_kb)

    elif message.text == 'Административный персонал':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Банки, Инвестиции, Лизинг':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Бухгалтерия, управленческий счёт, финансы предприятия':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Высший менеджмент':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Гос служба, некомерчиские организации':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Добыча сырья':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Домашний персонал':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Закупки':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Инсталяция и сервис':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Информационные технологии, интернет телеком':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Информационные технологии, интернет телеком':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Исскуство, развлечения, масс - медиа':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Консультирование':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Маркетинг, реклама, PR':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Медецина, фармацевтика':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Наука, образование':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Начало карьеры, студенты':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Продажи':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Производство, сельское хозяйство':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Рабочий персонал':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Спортивные клубы(фитнес и т.д)':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Страхование':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Строительство, недвижимость':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Транспорт, логистика':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Туризм, гостиницы, рестораны':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Треннинг управления персоналом':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)

    elif message.text == 'Юристы':
        await bot.send_message(message.from_user.id, 'Выберите фильтры--\n1ФИЛЬТР:\nОпыт работы -',
                               reply_markup=butnn.gret_kb)
        await filtersforproject.hp_job.set()

        @dp.message_handler(state=filtersforproject.hp_job)
        async def answer_q1(message: types.Message, state: FSMContext):
            hp_job = message.text
            await state.update_data(hp_job=hp_job)
            await message.answer('Выберите 2 фильтр\nПол\n(-_-)...?', reply_markup=butnn.hh_kb)
            await filtersforproject.tch_job.set()

        @dp.message_handler(state=filtersforproject.tch_job)
        async def answer_q2(message: types.Message, state: FSMContext):
            tch_job = message.text
            await state.update_data(tch_job=tch_job)
            await message.answer('Выберите 3 фильтр\nПол\n(-_-)...?', reply_markup=butnn.zants_kb)
            await filtersforproject.same.set()

        @dp.message_handler(state=filtersforproject.same)
        async def answer_q3(message: types.Message, state: FSMContext):
            same = message.text
            await state.update_data(same=same)
            await message.answer(f'Заполнение фильтров окончено, всё ли верно\n(-_-)...?')
            data = await state.get_data()
            text = '''1 Фильтр : {hp_job}\n2 Фильтр : {tch_job}\n3 Фильтр : {same}'''.format(
                hp_job=data.get('hp_job'),
                tch_job=data.get('tch_job'),
                same=data.get('same'),
            )
            await state.reset_state(with_data=False)
            await message.answer(text=text)

        @dp.message_handler()
        async def e_else(message, state):
            data = await state.get_data()
            await message.answer('Вы закончили выбор фильтров. 1 Фильтр {hp_job}'.format(data),
                                 reply_markup=butnn.hh_kb)





if __name__ == '__main__':
    executor.start_polling(dp)
