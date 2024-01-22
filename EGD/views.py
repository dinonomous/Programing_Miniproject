from django.shortcuts import render
from django.http import HttpRequest

def week1(request):
    videos = [
        {"title": "Question 1", "url": "https://www.youtube.com/embed/58oRZSB5LQk?autoplay=0&mute=1"},
        {"title": "Question 2", "url": "https://www.youtube.com/embed/4XjbZa1RW1o?autoplay=0&mute=1"},
        {"title": "Question 3", "url": "https://www.youtube.com/embed/w7__h9nyYTM?autoplay=0&mute=1"},
        {"PDF": "https://drive.google.com/file/d/19rtxMyOyUMXWFkAi1I-ANjxiwX21mdjm/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week2(request):
    videos = [
        {"title": "Question 1", "url": "https://www.youtube.com/embed/U0Dvyhu2psk?autoplay=0&mute=1"},
        {"title": "Question 2", "url": "https://www.youtube.com/embed/o8cZBsnjBi8?autoplay=0&mute=1"},
        {"title": "Question 3", "url": "https://www.youtube.com/embed/_Pn-wCtIMJw?autoplay=0&mute=1"},
        {"title": "Question 4", "url": "https://www.youtube.com/embed/oqPZCeXciQA?autoplay=0&mute=1"},
        {"title": "Question 5", "url": "https://www.youtube.com/embed/WCNwikX_LtQ?autoplay=0&mute=1"},
        {"title": "Question 6", "url": "https://www.youtube.com/embed/gd00u7hXZWk?autoplay=0&mute=1"},
        {"title": "Question 7", "url": "https://www.youtube.com/embed/VmmKCoaGe3Q?autoplay=0&mute=1"},
        {"title": "Question 8", "url": "https://www.youtube.com/embed/cfaQpcBxU50?autoplay=0&mute=1"},
        {"PDF": "https://drive.google.com/file/d/1QUcTP4VBTRBxB5ESTEnnpnVBVCzDc-Wy/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week3(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK3/1.mp4"},
        {"title": "Question 1(1)", "url": "/static/EGD/videos/WEEK3/1-1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK3/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK3/3.mp4"},
        {"PDF": "https://drive.google.com/file/d/1NInwnojarka-LJgAfCXsmkKTQYkHm2GQ/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week4(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK4/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK4/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK4/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK4/4.mp4"},
        {"PDF": "https://drive.google.com/drive/u/1/folders/1Az9mRgtfh3ZthCpXOuJKzZoWk2weG0-9/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week5(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK5/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK5/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK5/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK5/4.mp4"},
        {"PDF": "https://drive.google.com/file/d/1xOyEoQlQgojUNVQ1q-ur_dwJyRpsMFcl/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week6(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK6/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK6/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK6/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK6/4.mp4"},
        {"PDF": "https://drive.google.com/file/d/1_xk7XAg7w1qQLThnNcVeNS42wyTYqiHj/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week7(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK7/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK7/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK7/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK7/4.mp4"},
        {"PDF": "https://drive.google.com/file/d/1qpEevm2jmgQ5YGg45Lbp7Pw9o24y2J4I/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week8(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK8/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK8/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK8/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK8/4.mp4"},
        {"PDF": "https://drive.google.com/file/d/1ACV1hxKR6l23nrwd_HnieAGo-oaE-1Vu/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week9(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK9/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK9/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK9/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK9/4.mp4"},
        {"PDF": "https://drive.google.com/file/d/1EgWesZ2m2-msVY1ahXoorTMehzGVaDAf/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week10(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK10/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK10/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK10/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK10/4.mp4"},
        {"PDF": "https://drive.google.com/file/d/1VnMqvasdIA-lMhB6JTWrlUkWN6dHOEVM/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week11(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK11/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK11/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK11/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK11/4.mp4"},
        {"PDF": "https://drive.google.com/file/d/1Yk9lffK-eBMDRIQ59sHm5qdoXLVsA7S8/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})

def week12(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK12/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK12/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK12/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK12/4.mp4"},
        {"PDF": "https://drive.google.com/file/d/1SJe59EB0cKcW9kqNWAQq05nOCA7pA9PC/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})