import aiofiles
from pyrogram import Client

from io import BytesIO
import os

from ..config import CHUNK_SIZE
from ..database import get_channel

async def stream_to_file(client: Client, file_id, filename):
    async with aiofiles.open(filename, "ab") as f:
        stream = await client.get_file(file_id)
        async for chunk in stream:
            await f.write(chunk)

async def upload_file(client: Client, name):
    file = os.path.basename(name)
    file_ids = []
    with aiofiles.open(name, "rb") as f:
        size = os.path.getsize(name)
        remaining = size
        while remaining > 0:
            stream = BytesIO()
            stream.write(f.read(CHUNK_SIZE if remaining > CHUNK_SIZE else remaining))
            remaining -= CHUNK_SIZE
            stream.name = file
            file_ids.append((await client.save_file(stream)).id)
            stream.seek(0)
            stream.close()
    
    return (file_ids, file)

async def send_coded_info(client: Client, file_ids, file):
    return await client.send_message(get_channel(), f"Saved file\n{file_ids}\n{file}")

