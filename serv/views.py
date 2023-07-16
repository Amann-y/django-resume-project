from django.shortcuts import render

# Create your views here.

def services(request):
    context = {'services':'active','title':'Services'}
    return render(request, 'serv/services.html', context)
