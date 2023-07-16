from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'home':'active', 'title':'Home'}
    return render(request, 'core/home.html',context)


def contact(request):
    context = {'contact':'active','title':'Contact'}
    return render(request, 'core/contact.html',context)