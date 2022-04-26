from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json
import requests

# Create your views here.
def home(request):
    context = {
        "title": "GATES 2022 | GTBIT Official Techno-Cultural Fest Event for creative Souls",
    }
    return render(request,"index.html",context)

def about(request):
    context = {
        "title": "ABOUT | GATES 2022",
    }
    return render(request,"about.html",context)

def developer(request):
    context = {
        "title": "Developers | GATES 2022",
        "developers": [{
            "name": "Aanchal Rakheja",
            "title": "Full Stack developer",
            "desc": "Invest your time in technology and you will never regret",
            "email": "aanchalrakheja2001@gmail.com",
            "facebook" : "",
            "github" : "https://github.com/aanchalrakheja",
            "twitter" : "",
            "instagram" : "",
            "linkedIn":"www.linkedin.com/in/aanchal-rakheja2901",
            "image": "assets/developer/aanchal.png",
            "website": ""                 
        },{
            "name": "Garvit Vij",
            "title": "Full Stack Developer",
            "desc": "Effectuating ideas with innovation",
            "email": "garvit.vij.26@gmail.com",
            "facebook" : "https://www.facebook.com/garvit.vij.1",
            "github" : "https://github.com/garvitvij",
            "twitter" : "https://twitter.com/garvitvij",
            "instagram" : "https://www.instagram.com/garvit.vij_/",
            "linkedIn":"https://www.linkedin.com/in/Garvitvij",
            "image": "assets/developer/garvit.png",
            "website": ""                        
        },{
            "name": "Kanishk Chhabra",
            "title": "Android & Full Stack Web Developer",
            "desc": "I Love to Innovate and change lives using Science & Technology",
            "email": "kanishkchhabra23@gmail.com",
            "facebook" : "https://facebook.com/mrkc2303",
            "github" : "https://github.com/mrkc2303",
            "twitter" : "https://twitter.com/mrkc2303/",
            "instagram" : "https://www.instagram.com/kanishk_chhabra/",
            "linkedIn":"https://www.linkedin.com/in/kanishk-chhabra/",
            "image": "assets/developer/kanishk.png",
            "website": "https://www.kanishkchhabra.in/"                         
        },{
            "name": "Raghav Dhingra",
            "title": "Full Stack Developer",
            "desc": "Always try to solve a problem in a smarter way.",
            "email": "raghavdhingra.com",
            "facebook" : "",
            "github" : "",
            "twitter" : "",
            "instagram" : "",
            "linkedIn":"https://www.linkedin.com/in/raghav-dhingra/",
            "image": "assets/developer/raghav.png",
            "website": ""                        
        },{
            "name": "Ruhee Jain",
            "title": "Full Stack Web Developer",
            "desc": "Innovate. Create. Design. Inspire",
            "email": "ruhj707@gmail.com",
            "facebook" : "https://www.facebook.com/ruhee.jain16/",
            "github" : "https://github.com/Ruheej1",
            "twitter" : "https://twitter.com/Ruheejain_",
            "instagram" : "https://www.instagram.com/ruheejain_/",
            "linkedIn":"https://www.linkedin.com/in/ruhee-jain-47447b196/",
            "image": "assets/developer/ruhee.png",
            "website": ""                    
        },{
            "name": "Rupin Vijan",
            "title": "Full stack developer",
            "desc": "I am a web developer with impeccable working skills. Being a diligent learner, I have learnt Web Development  and I work hard to achieve the desired goal.",
            "email": "rupinvijan@gmail.com",
            "facebook" : "https://www.facebook.com/profile.php?id=100011423601329",
            "github" : "https://github.com/RupinVijan",
            "twitter" : "",
            "instagram" : "https://www.instagram.com/rupin_vijan/",
            "linkedIn":"https://www.linkedin.com/in/rupin-v-980b63118",
            "image": "assets/developer/rupin.png",
            "website": ""   
        },{
            "name": "Unnat Das",
            "title": "Front-end developer",
            "desc": "A Front-end developer and Competitive programmer, always keep trying to improve and be a better version of myself.",
            "email": "udas4153@gmail.com",
            "facebook" : "",
            "github" : "https://github.com/Sayo1305",
            "twitter" : "",
            "instagram" : "",
            "linkedIn":"https://www.linkedin.com/in/unnat-das-3b5374196/",
            "image": "assets/developer/unnat.png",
            "website": ""                          
        }],
    }
    return render(request,"developer.html",context)

def starNight(request):
    context = {
        "title": "STAR NIGHT | GATES 2022",
    }
    return render(request,"starNight.html",context)

def event(request):
    return redirect("/#event")

def getEvents(category,ImageUrl):
    new_event_list = []
    resp_data = requests.get("https://spreadsheets.google.com/feeds/list/1k315nuVJP8X6r8Cp2ANHbJEt1kXyp55s6WKHed8SlNY/1/public/full?alt=json")
    resp = json.loads(resp_data.text)
    event_list = resp["feed"]["entry"]
    for event in event_list:
        new_event = {}
        if event["gsx$eventcategory"]["$t"] == category:
            new_event["name"] = event["gsx$eventname"]["$t"]
            new_event["description"] = event["gsx$eventdescription"]["$t"]
            new_event["day"] = event["gsx$eventday"]["$t"]
            new_event["timing"] = event["gsx$eventtimings"]["$t"]
            new_event["duration"] = event["gsx$eventduration"]["$t"]
            new_event["category"] = event["gsx$eventcategory"]["$t"]
            new_event["link"] = event["gsx$registrationlink"]["$t"]
            if event["gsx$eventimageurl"]["$t"] == "":
                new_event["imageUrl"] = ImageUrl
            else:
                new_event["imageUrl"] = event["gsx$eventimageurl"]["$t"]
            new_event_list.append(new_event)
    return new_event_list

def techEvent(request):
    context = {
        "title": "Technical Events | GATES 2022",
    }
    event_list = getEvents("Technical","/static/assets/images/technical.jpg")
    context["events"] = event_list
    context["category"] = "Technical"
    return render(request,"https://linktr.ee/gdscweb",context)

def manageEvent(request):
    context = {
        "title": "Management Events | GATES 2022",
    }
    event_list = getEvents("Management","/static/assets/images/manage.jpg")
    context["events"] = event_list
    context["category"] = "Management"
    return render(request,"event.html",context)

def divineEvent(request):
    context = {
        "title": "Divine Events | GATES 2022",
    }
    event_list = getEvents("Divine","/static/assets/images/divine.jpg")
    context["events"] = event_list
    context["category"] = "Divine"
    return render(request,"event.html",context)

def miscEvent(request):
    context = {
        "title": "Miscellaneous Events | GATES 2022",
    }
    event_list = getEvents("Miscellaneous","/static/assets/images/misc.jpg")
    context["events"] = event_list
    context["category"] = "Miscellaneous"
    return render(request,"event.html",context)

def culturalEvent(request):
    context = {
        "title": "Cultural Events | GATES 2022",
    }
    event_list = getEvents("Cultural","/static/assets/images/cultural.jpg")
    context["events"] = event_list
    context["category"] = "Cutural"
    return render(request,"event.html",context)