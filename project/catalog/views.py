from django.shortcuts import render

def catalog_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
    return render(request, 'main/contacts.html')


def catalog_home(request):
    return render(request, 'main/home.html')
