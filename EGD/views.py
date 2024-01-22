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
        {"title": "Question 1", "url": "https://www.youtube.com/embed/YdMnqRKxdnY?autoplay=0&mute=1"},
        {"title": "Question 1(1)", "url": "https://www.youtube.com/embed/wcUsAvdjgPM?autoplay=0&mute=1"},
        {"title": "Question 2", "url": "https://www.youtube.com/embed/Jeb9V-3IMgQ?autoplay=0&mute=1"},
        {"title": "Question 3", "url": "https://www.youtube.com/embed/0455lV10G-I?autoplay=0&mute=1"},
        {"PDF": "https://drive.google.com/file/d/1NInwnojarka-LJgAfCXsmkKTQYkHm2GQ/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week4(request):
    videos = [
        {"title": "Question 1", "url": "https://www.youtube.com/embed/8PStUWML1Ng?autoplay=0&mute=1"},
        {"title": "Question 2", "url": "https://www.youtube.com/embed/N0otBPI40M4?autoplay=0&mute=1"},
        {"title": "Question 3", "url": "https://www.youtube.com/embed/Am6rESiJpGc?autoplay=0&mute=1"},
        {"title": "Question 4", "url": "https://www.youtube.com/embed/W0c6pN0rvKE?autoplay=0&mute=1"},
        {"PDF": "https://drive.google.com/drive/u/1/folders/1Az9mRgtfh3ZthCpXOuJKzZoWk2weG0-9/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week5(request):
    videos = [
        {"title": "Question 1", "url": "https://www.youtube.com/embed/XsvGz1pclWs?autoplay=0&mute=1"},
        {"title": "Question 2", "url": "https://www.youtube.com/embed/uhPXJDWShSI?autoplay=0&mute=1"},
        {"title": "Question 3", "url": "https://www.youtube.com/embed/pAbJgGKXPLM?autoplay=0&mute=1"},
        {"title": "Question 4", "url": "https://www.youtube.com/embed/b5lA8SIorvo?autoplay=0&mute=1"},
        {"PDF": "https://drive.google.com/file/d/1xOyEoQlQgojUNVQ1q-ur_dwJyRpsMFcl/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week6(request):
    videos = [
        {"title": "Question 1", "url": "https://www.youtube.com/embed/PGFAkWbaz6Y?autoplay=0&mute=1"},
        {"title": "Question 2", "url": "https://www.youtube.com/embed/AepHSF5Wqvs?autoplay=0&mute=1"},
        {"title": "Question 3", "url": "https://www.youtube.com/embed/TMXzKO8eKDo?autoplay=0&mute=1"},
        {"title": "Question 4", "url": "https://www.youtube.com/embed/7gEgs0l69cc?autoplay=0&mute=1"},
        {"PDF": "https://drive.google.com/file/d/1_xk7XAg7w1qQLThnNcVeNS42wyTYqiHj/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week7(request):
    videos = [
        {"title": "Question 1", "url": "https://www.youtube.com/embed/1mFq-pF6ri0?autoplay=0&mute=1"},
        {"title": "Question 2", "url": "https://www.youtube.com/embed/N7toggb5_a8?autoplay=0&mute=1"},
        {"title": "Question 3", "url": "https://www.youtube.com/embed/VcPB5Pg6otc?autoplay=0&mute=1"},
        {"title": "Question 4", "url": "https://www.youtube.com/embed/tkf-nREDO2M?autoplay=0&mute=1"},
        {"PDF": "https://drive.google.com/file/d/1qpEevm2jmgQ5YGg45Lbp7Pw9o24y2J4I/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week8(request):
    videos = [
        {"title": "Question 1", "url": "https://www.youtube.com/embed/nqM6iPfffkI?autoplay=0&mute=1"},
        {"title": "Question 2", "url": "https://www.youtube.com/embed/pIyBAL3JT-s?autoplay=0&mute=1"},
        {"title": "Question 3", "url": "https://www.youtube.com/embed/UmfsWLUONgc?autoplay=0&mute=1"},
        {"title": "Question 4", "url": "https://www.youtube.com/embed/XxpPGnaMENA?autoplay=0&mute=1"},
        {"PDF": "https://drive.google.com/file/d/1ACV1hxKR6l23nrwd_HnieAGo-oaE-1Vu/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week9(request):
    videos = [
        {"title": "Question 1", "url": "https://www.youtube.com/embed/2yJnmFKwdxs?autoplay=0&mute=1"},
        {"title": "Question 2", "url": "https://www.youtube.com/embed/rb8fesppNjA?autoplay=0&mute=1"},
        {"title": "Question 3", "url": "https://www.youtube.com/embed/p0L8O2x1ae8?autoplay=0&mute=1"},
        {"title": "Question 4", "url": "https://www.youtube.com/embed/scU9nj9dhaE?autoplay=0&mute=1"},
        {"PDF": "https://drive.google.com/file/d/1EgWesZ2m2-msVY1ahXoorTMehzGVaDAf/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week10(request):
    videos = [
        {"title": "Question 1", "url": "https://www.youtube.com/embed/Cz2LxZ6ZvME?autoplay=0&mute=1"},
        {"title": "Question 2", "url": "https://www.youtube.com/embed/imXFh-NX_qI?autoplay=0&mute=1"},
        {"title": "Question 3", "url": "https://www.youtube.com/embed/_qCd_0nzOFQ?autoplay=0&mute=1"},
        {"title": "Question 4", "url": "https://www.youtube.com/embed/mmetFAF9De8?autoplay=0&mute=1"},
        {"PDF": "https://drive.google.com/file/d/1VnMqvasdIA-lMhB6JTWrlUkWN6dHOEVM/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})


def week11(request):
    videos = [
        {"title": "Question 1", "url": "https://www.youtube.com/embed/58iwzOC6ugQ?autoplay=0&mute=1"},
        {"title": "Question 2", "url": "https://www.youtube.com/embed/dvKUTtyS4Oo?autoplay=0&mute=1"},
        {"title": "Question 3", "url": "https://www.youtube.com/embed/jwXeUroW_VU?autoplay=0&mute=1"},
        {"title": "Question 4", "url": "https://www.youtube.com/embed/X3uIcvUnj-w?autoplay=0&mute=1"},
        {"PDF": "https://drive.google.com/file/d/1Yk9lffK-eBMDRIQ59sHm5qdoXLVsA7S8/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})

def week12(request):
    videos = [
        {"title": "Question 1", "url": "https://www.youtube.com/embed/TYdHSEXQ9cE?autoplay=0&mute=1"},
        {"title": "Question 2", "url": "https://www.youtube.com/embed/5qtm0yWA24s?autoplay=0&mute=1"},
        {"title": "Question 3", "url": "https://www.youtube.com/embed/HrRImEO8fZY?autoplay=0&mute=1"},
        {"title": "Question 4", "url": "https://www.youtube.com/embed/5muzzI0NeS4?autoplay=0&mute=1"},
        {"PDF": "https://drive.google.com/file/d/1SJe59EB0cKcW9kqNWAQq05nOCA7pA9PC/preview"},
    ]

    return render(request, 'EGD.html', {'videos': videos})