from urllib.parse import urlparse, parse_qs
from yt_dlp import YoutubeDL


def clean_playlist_url(url: str) -> str:
    """
    Extract and rebuild a clean YouTube playlist URL.
    """

    parsed = urlparse(url)
    query = parse_qs(parsed.query)

    playlist_id = query.get("list")

    if not playlist_id:
        raise ValueError("No playlist ID found in URL.")

    return f"https://www.youtube.com/playlist?list={playlist_id[0]}"


def extract_playlist_videos(playlist_url: str) -> list[str]:
    clean_url = clean_playlist_url(playlist_url)
    
    
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "skip_download": True,
        "lazy_playlist": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(clean_url, download=False)

    if "entries" not in info:
        raise ValueError("Playlist extraction failed.")

    videos = []

    for entry in info["entries"]:
        if not entry:
            continue

        video_id = entry.get("id")

        if video_id:
            videos.append(
                f"https://www.youtube.com/watch?v={video_id}"
            )

    return videos


# # Example
# url = "https://www.youtube.com/watch?v=ccHcPhVBuuU&list=PLHJcMjLqJzkzHcKKd6p7BAfejlTpaozlv"

# videos = extract_playlist_videos(url)

# print(f"Found {len(videos)} videos")

# print(videos[:5])