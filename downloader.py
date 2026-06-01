from downloader_scripts.get_urls import *
from yt_dlp import YoutubeDL


def download_video(url: str):
    ydl_opts = {
        # Download best quality that is 480p or lower
        "format": (
            "bestvideo[height<=480]+bestaudio/"
            "best[height<=480]"
        ),

        "merge_output_format": "mp4",

        "outtmpl": "%(title)s.%(ext)s",

        "quiet": False,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        

playlist_url = "https://www.youtube.com/watch?v=ccHcPhVBuuU&list=PLHJcMjLqJzkzHcKKd6p7BAfejlTpaozlv"


urls = extract_playlist_videos(playlist_url)

print("number of videos: ", len(urls))
for url in urls:
    download_video(url)
    
# make the graphics engine that uses 2D arrays