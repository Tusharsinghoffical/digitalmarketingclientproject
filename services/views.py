from django.shortcuts import render

def index(request):
    return render(request, 'services/index.html')

def seo(request):
    return render(request, 'services/seo.html')

def ppc(request):
    return render(request, 'services/ppc.html')

def website_development(request):
    return render(request, 'services/website_development.html')

def apps(request):
    return render(request, 'services/apps.html')

def video_marketing(request):
    return render(request, 'services/video_marketing.html')