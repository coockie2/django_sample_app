from django.shortcuts import render, redirect
from django.contrib import messages
from upload_form.models import FileNameModel
import sys, os
import pandas as pd

UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'

def form(request):
    if request.method != 'POST':
        return render(request, 'upload_form/form.html')

    file = request.FILES['file']

    if file.name.endswith('.csv') == False:
        messages.error(request, 'CSV以外のファイルが選択されました！！')
        return render(request, 'upload_form/form.html')

    path = os.path.join(UPLOADE_DIR, file.name)
    with open(path, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    # pandasでcsv読み込み
    print(pd.read_csv(path))
    messages.success(request, 'ファイルのアップロードに成功しました！！')

    return render(request, 'upload_form/form.html')