import os
import aiormq
import asyncio
import logging
import httpx
from aiogram import Bot, types, Dispatcher

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

RABBITMQ_USER = os.environ.get('RABBITMQ_USER')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASS')
RABBITMQ_ADDRESS = os.environ.get('RABBITMQ_ADDRESS')
RABBITMQ_PORT = int(os.environ.get('RABBITMQ_PORT', 5672))
EXTERNAL_API_URL = os.environ.get('EXTERNAL_API_URL')
RABBITMQ_VHOST = os.environ.get('RABBITMQ_VHOST')
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
dp = Dispatcher()

channel = None
last_message = None


async def on_message(command):
    if command.body == b'print':
        logger.info(f'Last message: {last_message}')
    elif command.body == b'send':
        async with httpx.AsyncClient() as client:
            response = await client.post(EXTERNAL_API_URL, json={'last_message': last_message})
            logger.info(response)


@dp.message()
async def handle_message(message: types.Message):
    global last_message
    last_message = message.text
    ok = await channel.basic_publish(b'print', routing_key='0')
    logger.info(f" [x] Sent {last_message}")


async def main():
    global channel
    connection_string = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_ADDRESS}:{RABBITMQ_PORT}/{RABBITMQ_VHOST}"
    logger.info(connection_string)
    connection = await aiormq.connect(connection_string)
    channel = await connection.channel()

    declare_0 = await channel.queue_declare('0')

    await channel.basic_consume(
        declare_0.queue, on_message, no_ack=True
    )

    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info("Starting telegram bot...")
    asyncio.run(main())
