from get_urls import *
from yt_dlp import YoutubeDL


def download_video(url: str):
    ydl_opts = {
        # Download best quality that is 480p or lower
        "format": (
            "bestvideo[height<=480]+bestaudio/"
            "best[height<=480]"
        ),

        "merge_output_format": "mp4",
        "cookies-from-browser": True,

        "outtmpl": "%(title)s.%(ext)s",
        "quiet": False, 
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
        
        
playlist_url = "REPLACE_WITH_YOUR_PLAYLIST_URL"
urls = extract_playlist_videos(playlist_url)

print("number of videos: ", len(urls))
failed = []

for url in urls:
    try:
        download_video(url)
    except:
        print("="*50, "ERROR WHILE DOWNLOADING THIS VIDEO: ", url, "... WE WILL TRY AGAIN AFTER FINISHING THE REST", "="*50)
        failed.append(url)
    

if failed != []:
    print("RE-DOWNLOADING FAILED VIDEOS")
    
    for failed_url in failed:
        try:
            download_video(failed_url)
            failed.remove(url)
            
        except:
            print("="*50, "SECOND ATTEMPT: ", url, "="*50)

    
    print("Couldn't download these vidoes: ")
    print(failed)

else:
    print("Downloading finished without problems")