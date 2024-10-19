from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from TelegramBot.core.utils.statesform import StepsForm


async def get_form(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, lets start filling out the form. Enter your name')
    await state.set_state(StepsForm.GET_NAME)


async def get_name(message: Message, state: FSMContext):
    await message.answer(f'You name \r\n{message.text}\r\nNow enter your last name.')
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_LAST_NAME)


async def get_last_name(message: Message, state: FSMContext):
    await message.answer(f'Your last name \r\n{message.text}\r\nNow enter your age')
    await state.update_data(last_name=message.text)
    await state.set_state(StepsForm.GET_AGE)


async def get_age(message: Message, state: FSMContext):
    await message.answer(f'Your age \r\n{message.text}\r\n')
    context_data = await state.get_data()
    await message.answer(f'Stored data in the state machine: \r\n{str(context_data)}')
    name = context_data.get('name')
    last_name = context_data.get('last_name')
    data_user = f'Here is your data\r\n' \
                f'Name {name}\r\n' \
                f'Last name {last_name}\r\n' \
                f'Age {message.text}'
    await message.answer(data_user)
    await state.clear()

