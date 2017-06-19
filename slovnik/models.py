from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_name_short = models.CharField(max_length=25, unique=True)
    image = models.ImageField(upload_to='category_thumbnails', null=True, blank=True)

    def __str__(self):
        return self.category_name


class Word(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    word_name = models.CharField(max_length=100)
    word_name_short = models.CharField(max_length=25)
    image = models.ImageField(upload_to='words_images')
    audio = models.FileField(upload_to='words_audio', null=True, blank=True)

    def __str__(self):
        return self.word_name


class User(models.Model):
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Practise - Tests

class TestFourImages(models.Model):
    test_date = models.DateTimeField('date taken')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.category.category_name + " - " + self.test_date.strftime('%Y-%m-%d')


class TestFourImagesItem(models.Model):
    test = models.ForeignKey(TestFourImages, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='given_word')
    word_selected = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='selected_word')

    def __str__(self):
        return self.word.word_name + " - " + self.word_selected.word_name
