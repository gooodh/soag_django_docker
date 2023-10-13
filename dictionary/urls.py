from django.urls import path
from .views import home_page_view, add_word, read_from_file


urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('', home_page_view, name='home'),
    path('home/', home_page_view, name='home'),
    path('add_word/', add_word, name='add_word'),
    path('words_list/', read_from_file, name='words_list')
]
