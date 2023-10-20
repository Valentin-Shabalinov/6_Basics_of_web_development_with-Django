from django.shortcuts import render

def catalog_contacts(request):
    return render(request, 'main/contacts.html')


def catalog_home(request):
    return render(request, 'main/home.html')
