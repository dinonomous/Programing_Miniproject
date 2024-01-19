from django.shortcuts import render
from django.http import HttpRequest

def week1(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK1/question1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK1/question2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK1/question3.mp4"},
        {"PDF": "/static/EGD/videos/WEEK1/W1.pdf"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week2(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK2/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK2/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK2/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK2/4.mp4"},
        {"title": "Question 5", "url": "/static/EGD/videos/WEEK2/5.mp4"},
        {"title": "Question 6", "url": "/static/EGD/videos/WEEK2/6.mp4"},
        {"title": "Question 7", "url": "/static/EGD/videos/WEEK2/7.mp4"},
        {"title": "Question 8", "url": "/static/EGD/videos/WEEK2/8.mp4"},
        {"PDF": "/static/EGD/videos/WEEK2/W2.pdf"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week3(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK3/1.mp4"},
        {"title": "Question 1(1)", "url": "/static/EGD/videos/WEEK3/1-1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK3/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK3/3.mp4"},
        {"PDF": "/static/EGD/videos/WEEK3/W3.pdf"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week4(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK4/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK4/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK4/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK4/4.mp4"},
        {"PDF": "/static/EGD/videos/WEEK4/W4.pdf"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week5(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK5/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK5/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK5/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK5/4.mp4"},
        {"PDF": "/static/EGD/videos/WEEK5/W5.pdf"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week6(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK6/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK6/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK6/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK6/4.mp4"},
        {"PDF": "/static/EGD/videos/WEEK6/W6.pdf"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week7(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK7/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK7/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK7/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK7/4.mp4"},
        {"PDF": "/static/EGD/videos/WEEK7/W7.pdf"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week8(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK8/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK8/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK8/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK8/4.mp4"},
        {"PDF": "/static/EGD/videos/WEEK8/W8.pdf"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week9(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK9/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK9/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK9/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK9/4.mp4"},
        {"PDF": "/static/EGD/videos/WEEK9/W9.pdf"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week10(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK10/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK10/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK10/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK10/4.mp4"},
        {"PDF": "/static/EGD/videos/WEEK10/W10.pdf"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week11(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK11/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK11/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK11/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK11/4.mp4"},
        {"PDF": "/static/EGD/videos/WEEK11/W11.pdf"},
    ]

    return render(request, 'EGD.html', {'videos': videos})

def week12(request):
    videos = [
        {"title": "Question 1", "url": "/static/EGD/videos/WEEK12/1.mp4"},
        {"title": "Question 2", "url": "/static/EGD/videos/WEEK12/2.mp4"},
        {"title": "Question 3", "url": "/static/EGD/videos/WEEK12/3.mp4"},
        {"title": "Question 4", "url": "/static/EGD/videos/WEEK12/4.mp4"},
        {"PDF": "/static/EGD/videos/WEEK12/W12.pdf"},
    ]

    return render(request, 'EGD.html', {'videos': videos})