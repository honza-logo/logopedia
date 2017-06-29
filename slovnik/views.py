from django.views import generic
from slovnik.models import *
from slovnik import utils
from random import randint
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime


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
    slug_url_kwarg = 'cat'

    SESSION_TEST_ID = 'four_images_session_id_'

    MAX_COUNT = 10
    model = Category
    template_name = 'slovnik/test_four_images.html'
    slug_field = 'category_name_short'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.init_sessions()
        cat = self.kwargs[self.slug_url_kwarg]

        # First run of the View with brand new test: init models
        if self.request.session[self.SESSION_TEST_ID+cat] == 0:
            user = User.objects.first()
            category = Category.objects.get(category_name_short=cat)
            test = TestFourImages.objects.create(test_date=datetime.date.today(), user=user, category=category,
                                                 finished=False)
            self.request.session[self.SESSION_TEST_ID+cat] = test.id

            # Generate first set of test Words
            words = utils.generate_four_images(cat, [])
            # Insert into db
            TestFourImagesItem.objects.create(test=test, word_correct=words[0], word_selected=None, word_other_first=words[1],
                                              word_other_second=words[2], word_other_third=words[3], word_position=1,
                                              word_correct_position=randint(0, 3))

        # Display the latest entry in the DB
        test = TestFourImages.objects.get(id=self.request.session[self.SESSION_TEST_ID+cat])
        last_item = TestFourImagesItem.objects.filter(test=test).order_by('-word_position').first()

        context['correct_word'] = last_item.word_correct
        context['selected_words'] = [last_item.word_other_first, last_item.word_other_second,
                                     last_item.word_other_third]
        # Ensure consistency of displaying the correct word on the same position
        context['selected_words'].insert(last_item.word_correct_position, context['correct_word'])

        # Add the progress bar to show correct/incorrect past answers
        progress = []
        for item in TestFourImagesItem.objects.filter(test=test).order_by('word_position'):
            if item.word_selected == item.word_correct:
                progress.append("- ANO -")
            else:
                progress.append("- NE -")
        progress = progress[:-1]
        for i in range(len(progress), self.MAX_COUNT):
            progress.append("- O -")
        context['comparison_list'] = progress

        return context

    def post(self, request, *args, **kwargs):

        selected_word = request.POST['selected']
        cat = kwargs[self.slug_url_kwarg]

        test = TestFourImages.objects.get(id=self.request.session[self.SESSION_TEST_ID+cat])
        last_item = TestFourImagesItem.objects.filter(test=test).order_by('-word_position').first()
        last_item.word_selected = Word.objects.get(id=selected_word)
        last_item.save()

        pos = last_item.word_position + 1

        # If position is over the max count of items in test go to the result page
        if pos > self.MAX_COUNT:
            return HttpResponseRedirect(reverse('slovnik:test-four-images-results', args=(cat,)))

        # Generate new set of words for next item (exclude used words)
        past_images = TestFourImagesItem.objects.filter(test=test)
        image_id_list = []
        for item in past_images:
            image_id_list.append(item.word_correct.id)
        words = utils.generate_four_images(cat, image_id_list)
        # Insert into db
        TestFourImagesItem.objects.create(test=test, word_correct=words[0], word_selected=None,
                                          word_other_first=words[1],
                                          word_other_second=words[2], word_other_third=words[3], word_position=pos,
                                          word_correct_position=randint(0, 3))

        return HttpResponseRedirect(reverse('slovnik:test-four-images', args=(cat,)))

    def init_sessions(self):
        cat = self.kwargs[self.slug_url_kwarg]

        try:
            self.request.session[self.SESSION_TEST_ID+cat]
        except KeyError:
            self.request.session[self.SESSION_TEST_ID+cat] = 0


class TestFourImagesResultsView(generic.DetailView):
    slug_url_kwarg = 'cat'

    SESSION_TEST_ID = 'four_images_session_id_'

    model = Category
    template_name = 'slovnik/test_four_images_results.html'
    slug_field = 'category_name_short'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = self.kwargs[self.slug_url_kwarg]

        try:
            test = TestFourImages.objects.get(id=self.request.session[self.SESSION_TEST_ID + cat])
            context['result_set'] = TestFourImagesItem.objects.filter(test=test).order_by('word_position')
            self.del_sessions()
        except KeyError:
            context['redirect'] = 1

        return context

    def del_sessions(self):
        cat = self.kwargs[self.slug_url_kwarg]
        try:
            del self.request.session[TestFourImagesView.SESSION_TEST_ID+cat]
        except KeyError:
            pass


class RatingIndexView(generic.TemplateView):
    template_name = 'slovnik/rating_index.html'

    def post(self, request, *args, **kwargs):
        user = request.POST['user']
        try:
            RatingUser.objects.get(user=user)
        except RatingUser.DoesNotExist:
            RatingUser.objects.create(user=user)
        request.session['rating_user'] = user
        return HttpResponseRedirect(reverse('slovnik:rating-images'))


class RatingImagesView(generic.TemplateView):
    template_name = 'slovnik/rating_images.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        image = utils.get_image_for_user(self.request.session['rating_user'])
        print(image)
        done = 0
        if image is None:
            done = 1

        context['done'] = done
        context['image'] = image

        return context

    def post(self, request, *args, **kwargs):
        user = RatingUser.objects.get(user=request.session['rating_user'])

        word1 = request.POST['name1']
        word2 = request.POST['name2']
        word3 = request.POST['name3']
        image = RatingImages.objects.get(id=request.POST['image_id'])

        RatingChoices.objects.create(user=user, image=image, choice1=word1, choice2=word2, choice3=word3)

        return HttpResponseRedirect(reverse('slovnik:rating-images'))


class RatingResultsView(generic.TemplateView):
    template_name = 'slovnik/rating_results.html'

    