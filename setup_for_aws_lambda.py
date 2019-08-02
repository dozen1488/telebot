
import platform
from shutil import copyfile

def copy_ffmpeg_to_temp_folder(temp_folder):
    converter_path = None
    if "Windows" in platform.architecture()[1]:
        converter_path = "./static_files/ffmpeg.exe"
    else:
        converter_path = "./static_files/ffmpeg"
    executor_path = temp_folder + "/ffmpeg"
    try:
        st = os.stat(executor_path)
        os.chmod(executor_path, st.st_mode | stat.S_IEXEC)
    except:
        copyfile(converter_path, executor_path)
    return executor_path
