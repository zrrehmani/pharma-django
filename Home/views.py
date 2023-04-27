from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
class Home:
    def home(request):
        return render(request, 'Home/home.html')
