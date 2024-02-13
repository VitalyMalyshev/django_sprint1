from django.shortcuts import render


# Проверить какие аргументы принимают функции и должны быть ли в них доп аргументы(кроме индекс) и что еще в теле...
def about(request):
    template = 'pages/about.html'
    return render(request, template)

def rules(request):
    template = 'pages/rules.html'
    return render(request, template)
