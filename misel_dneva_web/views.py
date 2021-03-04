from django.shortcuts import render

# Create your views here.

app_name = 'misel_dneva_web'
def index(request):
  return render(request, 'daily_thoughts/index.html')

def search(request):
  return render(request, 'daily_thoughts/search.html')

def signin(request):
  return render(request, 'daily_thoughts/signin.html')

def video_id(request):
  return render(request, 'daily_thoughts/video_id.html')
