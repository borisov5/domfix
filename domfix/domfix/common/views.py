from django.shortcuts import render


def index(request):
    return render(request, 'common/index.html')


def contacts_page(request):
    return render(request, 'common/contacts-page.html')