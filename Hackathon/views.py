from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def Contest(request):
    return HttpResponse("Please Login")
def Contest_Day2(request):
    if request.method == "GET":
        return render(request, 'Hackathon/Contest_Day2.html')

    if request.method == "POST":
        name = request.POST['u']
        passw = request.POST['p']

        if name == 'halima' and passw == 'halima#01':
            return render(request, 'Hackathon/home.html')
        else:
            return render(request, 'Hackathon/Unseccessful.html')
