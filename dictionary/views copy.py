from django.views.generic import TemplateView

from django.http import HttpResponse
from django.shortcuts import render


# def upload_file(request):
#     return render(request, 'file.txt')

class HomePageView(TemplateView):
    template_name = 'home.html'


def upload_file(request):
    if request.method == "POST":
        with open("file.txt", "a", encoding="utf-8") as file:
            file.write(word1 + "-" + word2 + "\n")
    else:
        file = open("file.txt", "r", encoding="utf-8").read().splitlines()
        words1 = []
        words2 = []
        for line in file:
            word1, word2 = line.split("-")
            words1.append(word1)
            words2.append(word2)



#         return words1, words2
#     def add_to_file(word1: str, word2: str):
#         with open("file.txt", "a", encoding="utf-8") as file:
#             file.write(word1 + "-" + word2 + "\n")

#     def read_from_file():
#         file = open("file.txt", "r", encoding="utf-8").read().splitlines()
#         words1 = []
#         words2 = []
#         for line in file:
#             word1, word2 = line.split("-")
#             words1.append(word1)
#             words2.append(word2)
#         return words1, words2

#     print(read_from_file())
