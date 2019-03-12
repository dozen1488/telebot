import subprocess

def convert(voice_ogg_content):
    completedProcess = subprocess.run(
        ["./ffmpeg.exe", "-i", "pipe:0", "-f", "wav", "pipe:1"],
        input=voice_ogg_content,
        capture_output=True
    )
    return completedProcess.stdout