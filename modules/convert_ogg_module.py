import subprocess
import asyncio
import functools

from helpers import asyncronize_function

async def convert(voice_ogg_content):
    loop = asyncio.get_event_loop()
    completedProcess = await asyncronize_function(
        subprocess.run,
        ["./ffmpeg.exe", "-i", "pipe:0", "-f", "wav", "pipe:1"],
        input=voice_ogg_content,
        capture_output=True
    )
    return completedProcess.stdout