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


class TestVariant(models.Model):
    test_name = models.CharField(max_length=100)
    test_name_short = models.CharField(max_length=25)
    test_visible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='test_thumbnails', null=True, blank=True)

    def __str__(self):
        return self.test_name
