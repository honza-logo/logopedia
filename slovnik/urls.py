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
    # Will not be included
    # url(r'^learn/(?P<cat>[a-z0-9]+)/$', views.CategoryView.as_view(), name='category'),


    # ex /slovnik/learn/nabytek/zidle
    # detail of single word to learn
    url(r'^learn/(?P<cat>[a-z0-9]+)/(?P<word>[a-z0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # Block of tests

    # ex /slovnik/practice/four-images/
    # list of categories in test four images
    url(r'^practice/four-images/$', views.TestFourImagesCategoriesView.as_view(),
        name='test-four-images-categories'),

    # ex /slovnik/practice/four-images/obleceni
    # detail of single word to learn
    url(r'^practice/four-images/(?P<cat>[a-z0-9]+)/$', views.TestFourImagesView.as_view(),
        name='test-four-images'),

    # ex /slovnik/practice/four-images/obleceni/result
    # detail of single word to learn
    url(r'^practice/four-images/(?P<cat>[a-z0-9]+)/results/$', views.TestFourImagesResultsView.as_view(),
        name='test-four-images-results'),

    # image ratings:
    url(r'^rate/$', views.RatingIndexView.as_view(), name='rating-index'),
    url(r'^rate-images/$', views.RatingImagesView.as_view(), name='rating-images'),
    url(r'^rate-results/$', views.RatingResultsView.as_view(), name='rating-results'),
    url(r'^rate-newuser/$', views.RatingNewUserView.as_view(), name='rating-newuser'),
    url(r'^rate-logout/$', views.RatingLogoutView.as_view(), name='rating-logout'),
    url(r'^import/$', views.ImportView.as_view(), name='import'),
]
