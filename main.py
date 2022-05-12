from pytube import YouTube, Playlist, Channel
from pytube.exceptions import VideoUnavailable

def video_download(url):
    try:
        video = YouTube(url) #on_complete_callback=, on_complete_callback=
    except VideoUnavailable:
        print(f"Unable to download " + str(video.title))
    else:
        print("Downloading: " + str(video.title))
        video.streams.get_highest_resolution().download()

def playlist_download(url):
    playlist = Playlist(url)
    total_videos_in_playlist = len(playlist)
    if not total_videos_in_playlist:
        print("Empty playlist")
        return 
    count = 1
    for p in playlist.videos:
        print(f"Downloading {count}/{total_videos_in_playlist}: " + str(p.title))
        p.streams.get_highest_resolution().download()
        count+=1

def channel_download(url):
    channel = Channel(url)
    total_videos_in_channel = len(channel)
    if not total_videos_in_channel:
        print("Channel contains no videos")
        return
    count = 1
    for c in channel.videos:
        print(f"Downloading {count}/{total_videos_in_channel}: " + str(c.title))
        c.streams.get_highest_resolution().download()
        count+=1

option = input("Enter [v/p/c]: ")
if option=='v' or option=='V':
    url = input("Enter the video link: ")
    video_download(url)
elif option=='p' or option=='P':
    url = input("Enter the playlist link: ")
    playlist_download(url)
elif option=='c' or option=='C':
    url = input("Enter the channel link: ")
    channel_download(url)

print("Video(s) downloaded")