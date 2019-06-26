from django.shortcuts import render


def about(request):
    return render(request, 'home/about.html')


def robot(request):
    return render(request, 'home/Robots.txt')
