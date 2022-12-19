from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from pytube import YouTube
import os
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def movies(request):
    url = "https://www.imdb.com/chart/moviemeter/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table', {'class': 'chart full-width'})
    rows = table.find_all('tr')
    movies = []
    for row in rows:
        image = row.find('img')
        if image:
            movies.append(image['alt'])
    return render(request, "movies.html", {'movies': movies})


def youtube(request):
    try:
        if request.method == 'POST':
            try:
                getYouTubeVideoUrl = request.POST['tube_url']

                passUrlToYoutubeConstructor = YouTube(str(getYouTubeVideoUrl))

                # Extract Audio
                extractAudio = passUrlToYoutubeConstructor.streams.filter(only_audio=True).first()

                destination = request.POST['destination']

                # download the file
                output_file = extractAudio.download(output_path=destination)

                # save the download file

                basement, ext = os.path.splitext(output_file)
                new_mp3_file = basement + ".mp3"
                os.rename(output_file, new_mp3_file)

                # print("Download completed")
                return render(request, 'youtube.html', {'msg': 'Audio downloaded'})
            except:
                return render(request, 'youtube.html', {'msg': 'Audio is not downloaded'})

        return render(request, 'youtube.html', {'msg': ''})
    except:
        return render(request, "youtube.html", {"msg": "Sorry something went wrong!"})
