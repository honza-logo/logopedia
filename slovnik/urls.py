from django.conf.urls import url
from . import views

app_name = 'slovnik'
urlpatterns = [
    # ex /slovnik/
    # index - about the project learn / practice selection
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex /slovnik/practice/
    # chose what to train
    url(r'^practice/$', views.IndexView.as_view(), name='tests'),
    # ex /slovnik/learn/
    # section with different categories to learn new words
    url(r'^learn/$', views.LearnView.as_view(), name='learn'),
    # ex /slovnik/learn/nabytek/
    # detailed overview of selected dictionary category
    url(r'^learn/(?P<cat>[a-z0-9]+)/$', views.CategoryView.as_view(), name='category'),
    # ex /slovnik/learn/nabytek/1
    # detail of single word to learn
    url(r'^learn/(?P<cat>[a-z0-9]+)/(?P<word>[a-z]+)/$', views.DetailView.as_view(), name='detail'),
]
