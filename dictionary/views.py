from django.views.generic import TemplateView

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def home_page_view(request):
    return render(request, 'home.html')

def add_to_file(word1: str, word2: str):
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write(word1 + "-" + word2 + "\n")


def read_from_file(request):
    file = open("file.txt", "r", encoding="utf-8").read().splitlines()
    words1 = []
    words2 = []
    for line in file:

        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)
        words_list = {'data': zip(words1, words2)}
    return render(request, "words_list.html", words_list)


def add_word(request):
    if request.method == 'POST':
        add_to_file(request.POST['word1'], request.POST['word2'])
        return HttpResponseRedirect('/words_list')
    return render(request, 'add_word.html')
