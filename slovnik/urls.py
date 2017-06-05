from django.conf.urls import url
from . import views

app_name = 'slovnik'
urlpatterns = [
    # ex /slovnik/
    # index - about the project learn / practice selection
    url(r'^$', views.index, name='index'),
    # ex /slovnik/learn/
    # section with different categories to learn new words
    url(r'^learn/$', views.learn, name='learn'),
    # ex /slovnik/learn/nabytek/
    # detailed overview of selected dictionary category
    url(r'^learn/(?P<category>[a-z0-9]+)/$', views.category, name='category'),
    # ex /slovnik/learn/nabytek/1
    # detail of single word to learn
    url(r'^learn/(?P<category>[a-z0-9]+)/(?P<word_id>[0-9]+)/$', views.detail, name='word'),
]
