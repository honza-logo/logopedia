from django.views import generic
from slovnik.models import Category, Word, TestVariant
from slovnik import utils


class IndexView(generic.TemplateView):
    template_name = 'slovnik/index.html'


class LearnView(generic.ListView):
    template_name = 'slovnik/learn.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()


class PracticeView(generic.ListView):
    template_name = 'slovnik/practice.html'
    context_object_name = 'tests_list'

    def get_queryset(self):
        return TestVariant.objects.filter(test_visible=True)


class CategoryView(generic.DetailView):
    model = Category
    template_name = 'slovnik/category.html'
    slug_field = 'category_name_short'
    slug_url_kwarg = 'cat'


class TestTypeView(generic.ListView):
    template_name = 'slovnik/test.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = TestVariant.objects.get(test_name_short=self.kwargs['type'])
        return context


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


class TestDetailView(generic.DetailView):
    model = Word
    template_name = 'slovnik/test_detail.html'
    slug_field = 'word_name_short'
    slug_url_kwarg = 'cat'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

