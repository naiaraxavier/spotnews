from django.urls import path
from news.views import categories_form, index, news_details


urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", categories_form, name="categories-form"),
]
