from django.conf.urls import url
from . import views

app_name = 'slovnik'
urlpatterns = [
    # ex /slovnik/
    # index - about the project learn / practice selection
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex /slovnik/learn/
    # section with different categories to learn new words
    url(r'^learn/$', views.LearnView.as_view(), name='learn'),
    # ex /slovnik/practice/
    # choose what to train
    url(r'^practice/$', views.PracticeView.as_view(), name='practice'),
    # ex /slovnik/learn/nabytek/
    # detailed overview of selected dictionary category
    url(r'^learn/(?P<cat>[a-z0-9]+)/$', views.CategoryView.as_view(), name='category'),
    # ex /slovnik/practice/listening/
    # detailed overview of a test variant
    url(r'^practice/(?P<type>[a-z0-9]+)/$', views.TestTypeView.as_view(), name='test'),
    # ex /slovnik/learn/nabytek/1
    # detail of single word to learn
    url(r'^learn/(?P<cat>[a-z0-9]+)/(?P<word>[a-z0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex /slovnik/practice/basic/1
    # detail of single word to learn
    url(r'^practice/(?P<type>[a-z0-9]+)/(?P<cat>[a-z0-9]+)/(?P<pos>[0-9]+)$', views.TestDetailView.as_view(),
        name='test_detail'),
]
