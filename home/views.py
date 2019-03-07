from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    messages.success(request, 'Document deleted.')
    return render(request, 'home/index.html', {})
