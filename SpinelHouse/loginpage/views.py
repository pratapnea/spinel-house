from django.shortcuts import render, get_object_or_404

def login(request):
    return render(request, 'loginpage/login.html')