from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
import random

def home(request):
    return HttpResponse('<h1>공포 게임 커뮤니티</h1>')

class HomeView(View):
    def get(self , request, *args, **kwargs):
        number = str(random.randint(100,1000))
        # return HttpResponse('<h1>공포 게임 커뮤니티 ['+number+']!!!</h1>')
        # return HttpResponse('<h1>안녕하세요</h1><br><h3>랜덤숫자: '+number+'</h3>')
        # text = "<h1>Welcome</h1>"
        # text += '<h3>랜덤숫자</h3>['+number+']'
        # return HttpResponse(text)
        context = {
            "name" : "john" ,
             "int" : number ,
            "present" : "<ul><li>내용</li><li>내용2</li></ul>"
        }
        return render(request, "home.html" , context )