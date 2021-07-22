from django.http import HttpResponse

def index(request):
    test = "zapytanie"
    return HttpResponse(test)
