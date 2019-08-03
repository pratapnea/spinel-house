from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, HttpResponseRedirect

def homepage(request):
    #return HttpResponse("Thankyou")
    return render(request, 'indexpage/home.html')
