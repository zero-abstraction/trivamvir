from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def my_view(request):
    # Your logic here
    return HttpResponse("Welcome to Trivamvir!!!")
# Create your views here.
def api_status(request):
    data = {
        "status": "success",
        "message": "API is working fine"
    }
    return JsonResponse(data)
