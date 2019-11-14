from django.shortcuts import render


# wall for emil
def emil(request):
    return render(request, 'pong.html')


def about(request):
    return render(request, 'home/about.html')


def robot(request):
    return render(request, 'home/Robots.txt')
