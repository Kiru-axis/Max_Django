from django.shortcuts import render
from .models import Meetup
# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    return render(request,'meetups/index.html',{
        "meetups":meetups,
        
    })
# getting single meetups item
def meetup_details(request,meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        print(Meetup)
        return render(request,'meetups/meetup-details.html',{
            "meetup_found":False,
            "meetup-title":selected_meetup.title,
            "meetup-description":selected_meetup.description,
            "meetup-image":selected_meetup.image,
        })
    except Exception as exc:
        return render(request,'meetups/meetup-details.html',{
            "meetup_found":False,
        })
