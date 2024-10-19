from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ShippingOption, ShippingQuery


keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Pay order',
            pay=True
        )
    ],
    [
        InlineKeyboardButton(
            text='Link',
            url='https://nztcoder.com'
        )
    ]
])



EU_SHIPPING = ShippingOption(
    id='eu',
    title='Delivery to Europe',
    prices=[
        LabeledPrice(
            label='Delivery by Post Express',
            amount=500
        )
    ]
)




RU_SHIPPING = ShippingOption(
    id='ru',
    title='Delivery to Russia',
    prices=[
        LabeledPrice(
            label='Delivery by Russan post',
            amount=1500
        )
    ]
)





KZ_SHIPPING = ShippingOption(
    id='kz',
    title='Delivery to Kazakhstan',
    prices=[
        LabeledPrice(
            label='Delivery by KazPost',
            amount=800
        )
    ]
)




CITIES_SHIPPING = ShippingOption(
    id='capitals',
    title='Fast delivery in the city',
    prices=[
        LabeledPrice(
            label='Delivery by courier',
            amount=2000
        )
    ]
)


async def shipping_check(shipping_query: ShippingQuery, bot: Bot):
    shipping_options = []
    countries = ['EU', 'RU', 'KZ']
    if shipping_query.shipping_address.country_code not in countries:
        return await bot.answer_shipping_query(shipping_query.id, ok=False,
                                               error_message='We cannot deliver the package to your country')

    if shipping_query.shipping_address.country_code == 'EU':
        shipping_options.append(EU_SHIPPING)


    if shipping_query.shipping_address.country_code == 'RU':
        shipping_options.append(RU_SHIPPING)


    if shipping_query.shipping_address.country_code == 'KZ':
        shipping_options.append(KZ_SHIPPING)

    cities = ['Milan', 'Moskow', 'Astana']
    if shipping_query.shipping_address.city in cities:
        shipping_options.append(CITIES_SHIPPING)


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Purchase via Telegram Bot',
        description='Learning to accept payments via Telegram bot',
        payload='Payment through a bot',
        provider_token='410694247:TEST:4f25a852-9875-4f62-b645-0b61f5ab7440',
        currency='KZT',
        prices=[
            LabeledPrice(
                label='Access to classified information',
                amount=99000
            ),
            LabeledPrice(
                label='NDS',
                amount=20000
            ),
            LabeledPrice(
                label='Вiscount',
                amount=20000
            ),
            LabeledPrice(
                label='Bonus',
                amount=40000
            )
        ],
        max_tip_amount=5000,
        suggested_tip_amounts=[1000, 2000, 3000, 4000],
        start_parameter='nztcoder',
        provider_data=None,
        photo_url='https://almode.ru/uploads/posts/2023-05/1685253927_almode-ru-p-dostoprimechatelnosti-goroda-kaspi-29.jpg',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=False,
        need_phone_number=False,
        need_email=False,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=True,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=keyboards,
        request_timeout=15
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = f'Thank you for the payment {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.' \
          f'\r\nOur manager has received the request and is already dialing your phone number' \
          f'\r\nIn the meantime, you can download the digital version of our product - https://nztcoder.com'
    await message.answer(msg)


