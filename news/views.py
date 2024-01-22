from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from news.forms import CreateCategoryForm, CreateNewsForm
from news.models import Category, News


def index(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, id):
    try:
        news = get_object_or_404(News, id=id)
        categories = news.categories.all()
        author = news.author
        return render(
            request,
            "news_details.html",
            {"news": news, "categories": categories, "author": author},
        )
    except Http404:
        return render(request, "404.html")


def categories_form(request):
    form = CreateCategoryForm()

    if request.method == "POST":
        form = CreateCategoryForm(request.POST)

        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "categories_form.html", context)


def news_form(request):
    form = CreateNewsForm()

    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)

        if form.is_valid():
            # cria e salva uma instancia do modelo
            # commit=False -> não será salva imediatamente no banco
            instance = form.save(commit=False)
            # salva no banco
            instance.save()
            # salva os dados do formulário muitos
            # pra muitos corretamente no banco
            form.save_m2m()
            return redirect("home-page")

    context = {"form": form}

    return render(request, "news_form.html", context)
