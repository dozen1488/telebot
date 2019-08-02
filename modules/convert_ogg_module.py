import subprocess
import os
import stat
import platform

from helpers import asyncronize_function

def get_converter_name():
    converter_path = None
    if "Windows" in platform.architecture()[1]:
        converter_path = "./static_files/ffmpeg.exe"
    else:
        converter_path = "./static_files/ffmpeg"
        try:
            st = os.stat("./static_files/ffmpeg")
            os.chmod("./static_files/ffmpeg", st.st_mode | stat.S_IEXEC)
        except:
            pass
    return converter_path

async def convert(voice_ogg_content, converter_path):
    completedProcess = await asyncronize_function(
        subprocess.run,
        [converter_path, "-i", "pipe:0", "-f", "wav", "pipe:1"],
        input=voice_ogg_content,
        capture_output=True
    )
    return completedProcess.stdout