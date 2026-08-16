## What does this script do?
It lets you download YouTube playlists by passing its link.
If a video failes to download it retires to download it again after
finishing the rest of the playlist.
When the script finishes downloading the videos it will list all the videos that couldn't be downloaded.

## IMPORTANT NOTE:
Some videos might not download because its age restreticed, private or because
of a network error.


## How to use?
Copy your playlist url and put it in here:
```
playlist_url = "REPLACE_WITH_YOUR_PLAYLIST_URL"
```

and then run this command to start the script:
```
python downloader.py
```