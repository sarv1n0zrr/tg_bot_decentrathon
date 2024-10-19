from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from core.handlers.basic import get_start, get_photo, get_hello
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_fake_contact, get_true_contact
from core.settings import settings
import asyncpg
import asyncio
import logging  
from aiogram.filters import Command, CommandStart
from core.utils.commands import set_commands
from core.handlers.basic import get_location
from core.handlers.basic import get_inline
from core.handlers.callback import select_macbook
from core.utils.callbackdata import MacInfo
from core.handlers.pay import order, pre_checkout_query, successful_payment, shipping_check
from core.middlewares.countermiddleware import CounterMiddleware
from core.middlewares.officehours import OfficeHoursMiddleware
from core.middlewares.dbmiddleware import DbSession
from core.handlers import form
from core.utils.statesform import StepsForm
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text ='Bot started')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot stopped')


def create_pool():
    return asyncpg.create_pool(f"host=127.0.0.1 port=5432 dbname=users user=postgres password=sarvi007"
                                            f"connect_timeout=60")

    # return await asyncpg.create_pool(f"host=127.0.0.1 port=5432 dbname=users user=postgres password=sarvi007"
    #                                         f"connect_timeout=60")


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    pool_connect = create_pool()

    dp = Dispatcher()
    dp.update.middleware.register(DbSession(pool_connect))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(form.get_age, StepsForm.GET_AGE)
    dp.message.register(form.get_last_name, StepsForm.GET_LAST_NAME)
    dp.message.register(form.get_name, StepsForm.GET_NAME)
    dp.message.register(form.get_form, Command(commands='form'))
    dp.update.middleware.register(OfficeHoursMiddleware())
    dp.message.middleware.register(CounterMiddleware())
    dp.shipping_query.register(shipping_check)
    dp.message.register(order, Command(commands='pay'))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, F.successful_payment)
    dp.message.register(get_location, F.location)
    dp.message.register(get_inline, Command(commands='inline'))
    dp.callback_query.register(select_macbook,MacInfo.filter())
    # dp.message.register(get_photo, ContentTypesFilter(content_types=[ContentType.PHOTO]))
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == 'Hello')
    dp.message.register(get_true_contact, F.contact, IsTrueContact)
    dp.message.register(get_fake_contact, F.contact)
    # dp.message.register(get_true_contact, ContentTypesFilter(content_types=[ContentType.CONTACT], IsTrueContact()))
    # dp.message.register(get_fake_contact, ContentTypesFilter(content_types=[ContentType.CONTACT]))
    # dp.message.register(get_start, Command(commands=['start','run']))
    dp.message.register(get_start, CommandStart())
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
