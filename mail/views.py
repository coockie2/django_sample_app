from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    send_mail(
            "タイトル", \
            "本文です\nこんにちは。メールを送信しました", \
            "from@mail.com", \
            ["to@mail.com"])
    return HttpResponse('<h1>email send complete.</h1>')
