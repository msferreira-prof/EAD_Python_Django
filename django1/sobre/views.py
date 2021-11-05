from django.http import HttpResponse

# Create your views here.
def metodoSobre(request):
    return HttpResponse('/templates/index.html')