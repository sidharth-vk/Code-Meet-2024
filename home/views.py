from django.shortcuts import render,redirect
from .models import Event_Participant
# Create your views here.


def home(request):
    return render(request,'index.html')


def treasure_hunt(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        teamname = request.POST.get('teamname')
        phone = request.POST.get('phone')
        collegename = request.POST.get('collegename')
        event = request.POST.get('event', 'Treasure Hunt')  # Default to 'Treasure Hunt'

        # Create and save the new participant
        Event_Participant.objects.create(
            name=name,
            email=email,
            teamname=teamname,
            phone=phone,
            collegename=collegename,
            event=event
        )
        return render(request,'success.html') 
    return render(request,'events/treasurehunt.html')


def geo_guesser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        teamname = request.POST.get('teamname')
        phone = request.POST.get('phone')
        collegename = request.POST.get('collegename')
        event = request.POST.get('event', 'Treasure Hunt')  # Default to 'Treasure Hunt'

        # Create and save the new participant
        Event_Participant.objects.create(
            name=name,
            email=email,
            teamname=teamname,
            phone=phone,
            collegename=collegename,
            event=event
        )
        return render(request,'success.html') 
    return render(request,'events/geo_guesser.html')


def paper_pitch(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        teamname = request.POST.get('teamname')
        phone = request.POST.get('phone')
        collegename = request.POST.get('collegename')
        event = request.POST.get('event', 'Treasure Hunt')  # Default to 'Treasure Hunt'

        # Create and save the new participant
        Event_Participant.objects.create(
            name=name,
            email=email,
            teamname=teamname,
            phone=phone,
            collegename=collegename,
            event=event
        )
        return render(request,'success.html')  
    return render(request,'events/paper_pitch.html')


