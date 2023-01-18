from django.shortcuts import render

from django.http import HttpResponse
def blog(request):
    #blog->b_home so use / for change directory
    return render(request, "blog/b_index.html")