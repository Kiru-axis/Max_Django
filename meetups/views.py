from django.shortcuts import render

# Create your views here.
def index(request):
    meetups = [
        {"title": "A first Meetup",
        "locations": "Nairobi",
        "slug":"a-first-meetup"
        },
        {"title": "A second Meetup",
        "locations": "Accra",
        "slug":"a-second-meetup"
        },
        {"title": "A third Meetup",
        "locations": "Kigali",
        "slug":"a-third-meetup"
        },
    ]
    return render(request,'meetups/index.html',{
        "show_meetups":True,
        "meetups":meetups,
        
    })
def meetup_details(request,meetup_slug):
    print(meetup_slug)
    selected_meetup ={
        "title": "A first Meetup",
        "description": "These is a first meetup",
    }
    return render(request,'meetups/meetup-details.html',{
        "meetup-title":selected_meetup["title"],
        "meetup-description":selected_meetup["description"],
    })