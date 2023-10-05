import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types.bot_command import BotCommand
from aiogram.types.bot_command_scope_all_group_chats import BotCommandScopeAllGroupChats
from aiogram.types.bot_command_scope_all_private_chats import BotCommandScopeAllPrivateChats
from aiogram.methods import set_my_commands
from handlers import commands_01_02

logging.basicConfig(level=logging.DEBUG)
bot = Bot(token="")

async def main():
    await bot.set_my_commands(commands=[BotCommand(command="start", description="start")],
                                            scope=BotCommandScopeAllGroupChats())
    await bot.set_my_commands(commands=[BotCommand(command="command_02", description="command_02")],
                                            scope=BotCommandScopeAllPrivateChats())
    dp = Dispatcher()
    dp.include_routers(commands_01_02.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())