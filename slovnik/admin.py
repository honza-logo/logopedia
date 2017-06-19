from django.contrib import admin

from .models import Category, Word, TestVariant

admin.site.register(Category)
admin.site.register(Word)
admin.site.register(TestVariant)
