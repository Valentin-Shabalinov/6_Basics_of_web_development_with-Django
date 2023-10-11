from django.shortcuts import render

def catalog_contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        # а также передается информация, которую заполнил пользователь
        print(name)
    return render(request, 'main/contacts.html')


def catalog_home(request):
    return render(request, 'main/home.html')
