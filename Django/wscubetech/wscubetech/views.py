from django.http import HttpResponse
from django.shortcuts import render
from Subjects.models import Subjects
from Video.models import Video
from django.shortcuts import render, get_object_or_404


def aboutus(request):
    return HttpResponse('Welcome to wscube tech')

def subject(request):
    subjectData=Subjects.objects.all()
    subData = {
        'subjectData':subjectData
    } 
    return render(request, 'pages/subject.html',subData)


def aboutus(request):
    return render(request,'pages/aboutus.html', {'navbar': 'aboutus'})

def homepage(request):
    data = {
        'title' : 'home new'
    }
    return render(request,'index.html',data)


def tutorial(request):
    videoData=Video.objects.all()
    Data = {
        'videoData':videoData
        }
    return render(request, 'pages/tutorial.html',Data)


def subject_videos(request, subject_id):
    subject = get_object_or_404(Subjects, pk=subject_id)
    videos = Video.objects.filter(Subjects=subject)
    context = {'subject': subject, 'videos': videos}
    print(context,videos)
    return render(request, 'pages/subject.html', context)
