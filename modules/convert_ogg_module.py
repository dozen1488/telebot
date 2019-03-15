import subprocess
import os
import stat
import platform

from helpers import asyncronize_function

converter_path = None

if "Windows" in platform.architecture()[1]:
    converter_path = "./ffmpeg.exe"
else:
    converter_path = "./ffmpeg"
    st = os.stat("./ffmpeg")
    os.chmod("./ffmpeg", st.st_mode | stat.S_IEXEC)

async def convert(voice_ogg_content):
    completedProcess = await asyncronize_function(
        subprocess.run,
        [converter_path, "-i", "pipe:0", "-f", "wav", "pipe:1"],
        input=voice_ogg_content,
        capture_output=True
    )
    return completedProcess.stdout