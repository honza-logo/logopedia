from django.views import generic
from slovnik.models import Category, Word
from slovnik import utils
from random import randint


class IndexView(generic.TemplateView):
    template_name = 'slovnik/index.html'


class LearnView(generic.ListView):
    template_name = 'slovnik/learn.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()


class PracticeView(generic.TemplateView):
    template_name = 'slovnik/practice.html'


# Single view for category will not be used
# class CategoryView(generic.DetailView):
#     model = Category
#     template_name = 'slovnik/category.html'
#     slug_field = 'category_name_short'
#     slug_url_kwarg = 'cat'


class TestFourImagesCategoriesView(generic.ListView):
    template_name = 'slovnik/test_four_images_categories.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()


class DetailView(generic.DetailView):
    model = Word
    template_name = 'slovnik/detail.html'
    slug_field = 'word_name_short'
    slug_url_kwarg = 'word'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['word_details'] = utils.get_word_details(self.kwargs['cat'], self.kwargs['word'])
        return context


class TestFourImagesView(generic.DetailView):
    MAX_COUNT = 10
    model = Category
    template_name = 'slovnik/test_four_images.html'
    slug_field = 'category_name_short'
    slug_url_kwarg = 'cat'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            self.request.session['four_images_session_started']
        except KeyError:
            self.request.session['four_images_session_started'] = 1

        context['selected_words'] = utils.generate_four_images(self.kwargs['cat'], [])
        context['correct_word'] = context['selected_words'][randint(0, 3)]
        return context
