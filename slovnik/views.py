from django.views import generic
from slovnik.models import Category, Word
from slovnik import utils


class IndexView(generic.TemplateView):
    template_name = 'slovnik/index.html'


class LearnView(generic.ListView):
    template_name = 'slovnik/learn.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()


class CategoryView(generic.DetailView):
    model = Category
    template_name = 'slovnik/category.html'
    slug_field = 'category_short_name'
    slug_url_kwarg = 'cat'


class DetailView(generic.DetailView):
    model = Word
    template_name = 'slovnik/detail.html'
    slug_field = 'word_short_name'
    slug_url_kwarg = 'word'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['word_details'] = utils.get_word_details(self.kwargs['cat'], self.kwargs['word'])
        return context

