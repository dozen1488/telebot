import subprocess
import asyncio
import functools
import os
import stat

from helpers import asyncronize_function

st = os.stat("./ffmpeg.exe")
os.chmod("./ffmpeg.exe", st.st_mode | stat.S_IEXEC)

async def convert(voice_ogg_content):
    loop = asyncio.get_event_loop()
    completedProcess = await asyncronize_function(
        subprocess.run,
        ["./ffmpeg.exe", "-i", "pipe:0", "-f", "wav", "pipe:1"],
        input=voice_ogg_content,
        capture_output=True
    )
    return completedProcess.stdout