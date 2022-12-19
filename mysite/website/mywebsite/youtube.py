from pytube import YouTube
import os

getYouTubeVideoUrl = input("Enter the URL: ")

passUrlToYoutubeConstructor = YouTube(str(getYouTubeVideoUrl))

# Extract Audio
extractAudio = passUrlToYoutubeConstructor.streams.filter(only_audio=True).first()

destination = input("Enter the destination: ")

# download the file
output_file = extractAudio.download(output_path=destination)

# save the download file

basement, ext = os.path.splitext(output_file)
new_mp3_file = basement + ".mp3"
os.rename(output_file, new_mp3_file)

print("Download completed")