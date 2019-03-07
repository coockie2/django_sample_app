# -*- coding: utf-8 -*-
import os
import webbrowser
import abc

from django.conf import settings

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class BaseRender:

    def render(self):
        self.init()
        self.draw()
        self.after()

    def init(self):
        # 源真ゴシック（ http://jikasei.me/font/genshin/）
        ttf = os.path.join(settings.BASE_DIR, 'common', 'static/fonts/MS Gothic.ttf')

        # 白紙をつくる（A4縦）
        self.FILENAME = os.path.join(settings.BASE_DIR, 'common', 'static/pdf/' + self.filename())
        self.c = canvas.Canvas(self.FILENAME, pagesize=portrait(A4))

        # フォント登録
        pdfmetrics.registerFont(TTFont('font', ttf))
        self.font_size = 20
        self.c.setFont('font', self.font_size)

    @abc.abstractmethod
    def draw(self):
        raise NotImplementedError()

    def after(self):
        # Canvasに書き込み
        self.c.showPage()

        # ファイル保存
        self.c.save()

        # ブラウザーで表示
        webbrowser.open(self.FILENAME)

    @abc.abstractmethod
    def filename(self):
        raise NotImplementedError()
