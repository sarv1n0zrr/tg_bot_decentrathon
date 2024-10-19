from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Start to work'

        ),
        BotCommand(
            command='help',
            description='Help'
        ),
        BotCommand(
            command='cancel',
            description= 'Stop to work'
        ),
        BotCommand(
            command='inline',
            description='Show inline keyboard'
        ),
        BotCommand(
            command='pay',
            description='Buy product'
        ),
        BotCommand(
            command='form',
            description='Start quiz'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())



