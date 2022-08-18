import aiogram
from create_bot import dp
import handlers

async def on_startup(_):
    print('bot is activated..')

handlers.register_handlers_bot(dp)

if __name__ == '__main__':
    aiogram.utils.executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

