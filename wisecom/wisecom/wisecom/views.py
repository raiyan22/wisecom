from django.http import HttpResponse

def home_page(request):
    print("home running")
    return HttpResponse("Hello world!")