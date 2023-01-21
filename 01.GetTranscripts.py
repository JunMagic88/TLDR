import os
from pytube import Playlist, YouTube
from youtube_transcript_api import YouTubeTranscriptApi

# Create the "Texts" folder if it does not already exist
if not os.path.exists("Texts"):
    os.makedirs("Texts")

# Open the "00.YoutubeURLs.txt" file and read the URLs
with open("00.YoutubeURLs.txt", "r") as file:
    urls = file.readlines()

# Iterate through the URLs
for url in urls:
    url = url.strip()
    if "playlist?list=" in url:
        try:
            # Try creating a Playlist object
            playlist = Playlist(url)
            videos = playlist.videos
        except Exception as e:
            print(f"Error: {e}")
    elif "watch?v=" in url:
        video = YouTube(url)
        videos = [video]
    else:
        print("Invalid URL")
        continue

    # Save the SRT transcript from each video into separate files
    for video in videos:
        with open('Texts/'+video.title +'.txt', "w") as file:
            # Iterate through the videos and write their titles to the file
            srt = YouTubeTranscriptApi.get_transcript(video.video_id)
            text=""
            for item in srt:
                text = text+(item['text'])+" "
            file.write(video.title + "\n\n" +text)
