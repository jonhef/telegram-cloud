import asyncio
from pyrogram import Client

from config import *

async def main():
    async with Client("my_account", API_ID, API_HASH) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())