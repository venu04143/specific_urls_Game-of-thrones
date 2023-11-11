from django.shortcuts import render

# Create your views here.
def winterfell(request):
    return render(request,'starks.html')
