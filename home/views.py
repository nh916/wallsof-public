from django.shortcuts import render



def emil(request):
    return render(request, 'pong.html')


def about(request):
    return render(request, 'home/about.html')


def robot(request):
    return render(request, 'home/Robots.txt')
