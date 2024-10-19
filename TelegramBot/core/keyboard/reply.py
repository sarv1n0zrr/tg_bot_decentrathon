from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder
reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Row 1. Button 1'
        ),
        KeyboardButton(
            text='Row 1. Button 2'
        ),
        KeyboardButton(
            text='Row 1. Button 3'
        )
    ],
    [
        KeyboardButton(
            text='Row 2. Button 1'
        ),
        KeyboardButton(
            text='Row 2. Button 2'
        ),
        KeyboardButton(
            text='Row 2. Button 3'
        ),
        KeyboardButton(
            text='Row 2. Button 4'
        )
    ],
    [
        KeyboardButton(
            text='Row 3. Button 1'
        ),
        KeyboardButton(
            text='Row 3. Button 2'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Choose a button ↓', selective=True)

loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Send location',
            request_location=True
        )
    ],
    [
        KeyboardButton(
            text='Send my contact',
            request_contact=True
        )
    ],
    [
        KeyboardButton(
            text='Create a poll',
            request_poll=KeyboardButtonPollType()
        )
    ]
], resize_keyboard=True, one_time_keyboard=False,
   input_field_placeholder='Send your location, phone number or create a poll ↓' )

def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Button 1')
    keyboard_builder.button(text='Button 2')
    keyboard_builder.button(text='Button 3')
    keyboard_builder.button(text='Send location', request_location=True)
    keyboard_builder.button(text='Send contact', request_contact=True)
    keyboard_builder.button(text='Create a poll', request_poll=KeyboardButtonPollType())
    keyboard_builder.adjust(3, 2, 1)
    keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True,
                               input_field_placeholger='Send your location, phone number or create a poll ↓')



