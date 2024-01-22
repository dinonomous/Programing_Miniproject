from django.shortcuts import render
from django.http import HttpRequest

def unit1(request):
    videos = [
        {"title": "* Cell Theory", "url": "https://www.youtube.com/embed/-mPReow5Sjg?autoplay=0&mute=1"},###
        {"title": "* Cytoskeleton", "url": "https://www.youtube.com/embed/j7jASlS0298?autoplay=0&mute=1"},
        {"title": "* centriole", "url": "https://www.youtube.com/embed/e7p8jmvVPzY?autoplay=0&mute=1"},
        {"title": "* Homeostasis and Negative/Positive Feedback", "url": "https://www.youtube.com/embed/Iz0Q9nTZCw4?autoplay=0&mute=1"},
        {"title": "* Cell Cycle", "url": "https://www.youtube.com/embed/RYhBKl5Pm60?autoplay=0&mute=1"},
        {"title": "* Mitosis", "url": "https://www.youtube.com/embed/f-ldPgEfAHI?autoplay=0&mute=1"},
        {"title": "* Meiosis ", "url": "https://www.youtube.com/embed/VzDMG7ke69g?autoplay=0&mute=1"},
        {"title": "* Cell Differentiation and Stem cell", "url": "https://www.youtube.com/embed/t3g26p9Mh_k?autoplay=0&mute=1"},
    ]
    PDF = [
        {"name": "Material", "path": "https://drive.google.com/file/d/1JeVaJdGZXo7Dv8sgFKxFWqF83rAR3Wo6/preview"},
    ]

    # Pass the videos to the template
    context = {'videos': videos, 'PDF': PDF}

    # Render the HTML template with the data
    return render(request, 'computationalBiology.html', context)
##################################################################################################################################

def unit2(request):
    pass
def unit3(request):
    pass    
def unit4(request):
    pass
def unit5(request):
    pass