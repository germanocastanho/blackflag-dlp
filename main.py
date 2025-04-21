# Copyleft 🄯 2025, Germano Castanho;
# Software livre licenciado sob a GPL-3.0;
# Cada linha, um manifesto pela liberdade!


import time
import uuid
from pathlib import Path

import yt_dlp

VIDEOS = Path(__file__).parent / "videos"
VIDEOS.mkdir(exist_ok=True)
VIDEO = VIDEOS / f"{uuid.uuid4()}.mp4"


def get_video_url():
    print("Bem-vindo ao BlackFlag! 🏴")
    time.sleep(1)

    video_url = input("Insira a URL do vídeo: ")
    time.sleep(1)
    return video_url


def download_video(video_url):
    print("Iniciando download... ⏳")
    time.sleep(1)

    ydl_opts = {
        "format": "best",
        "outtmpl": f"{VIDEO}",
        "quiet": True,
        "http_headers": {
            "Referer": f"{video_url}",
            "User-Agent": "Chrome/134.0",
        },
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print("Download conluído! 🚀")
    except Exception as _:
        print("Erro no download! 😱")
    return None


if __name__ == "__main__":
    video_url = get_video_url()
    download_video(video_url)
