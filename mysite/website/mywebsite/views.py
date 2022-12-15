from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
def about(request):
    return render(request, 'about.html', {})
def discount(request):
    url = "https://www.imdb.com/chart/moviemeter/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table',  {'class': 'chart full-width'})
    rows = table.find_all('tr')
    movies = []
    for row in rows:
        image = row.find('img')
        if image:
            movies.append(image['alt'])
    return render(request, "discount.html", {'movies': movies})