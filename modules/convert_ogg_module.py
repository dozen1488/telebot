import subprocess
import asyncio
import functools

async def convert(voice_ogg_content):
    loop = asyncio.get_event_loop()
    completedProcess = await loop.run_in_executor(
        None,
        functools.partial(
            subprocess.run,
            ["./ffmpeg.exe", "-i", "pipe:0", "-f", "wav", "pipe:1"],
            input=voice_ogg_content,
            capture_output=True
        )
    )
    return completedProcess.stdout