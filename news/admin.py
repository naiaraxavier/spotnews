from django.contrib import admin
from news.models import Category, News, User

# Register your models here.
admin.site.register(Category)
admin.site.register(User)
admin.site.register(News)
