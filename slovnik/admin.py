from django.contrib import admin
from .models import Category, Word, User, TestFourImages, TestFourImagesItem, RatingUser, RatingImages, RatingChoices

admin.site.register(Category)
admin.site.register(Word)
admin.site.register(User)
admin.site.register(TestFourImages)
admin.site.register(TestFourImagesItem)
admin.site.register(RatingUser)
admin.site.register(RatingImages)
admin.site.register(RatingChoices)
