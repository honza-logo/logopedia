from django.contrib import admin
from .models import Category, Word, User, TestFourImages, TestFourImagesItem

admin.site.register(Category)
admin.site.register(Word)
admin.site.register(User)
admin.site.register(TestFourImages)
admin.site.register(TestFourImagesItem)
