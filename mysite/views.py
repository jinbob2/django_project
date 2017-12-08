from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

# def team(request):
#     text="<h1>팀장 : John</h1>"
#     text+="<h2>팀원 : Jame</h2>"
#     return HttpResponse(text)

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request , "home.html" , { } )

class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request , "Base.html" , { } )

class Team(View):
    def get(self, request, *args, **kwargs):
        return render(request , "Team.html", { } )
