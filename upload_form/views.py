from django.shortcuts import render, redirect
from upload_form.models import FileNameModel
import sys, os
import pandas as pd

UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'

def form(request):
    if request.method != 'POST':
        return render(request, 'upload_form/form.html')

    file = request.FILES['file']
    path = os.path.join(UPLOADE_DIR, file.name)
    with open(path, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    # pandasでcsv読み込み
    print(pd.read_csv(path))

    return redirect('upload_form:complete')

def complete(request):
    return render(request, 'upload_form/complete.html')
