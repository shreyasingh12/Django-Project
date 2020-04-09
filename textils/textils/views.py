#i have created this file.

from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Hello shreya</h1> <a href="https://www.youtube.com/
    watch?v=zs2Ux1jfDD0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=6" >heyyy</a>''')


def about(request):
    return HttpResponse("about shreya")