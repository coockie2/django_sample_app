# -*- coding: utf-8 -*-
import io
import os

from django.conf import settings
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

from .models import Friend, Message
from .forms import FriendForm, MessageForm

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import webbrowser


# Pythonでディレクトリの上層にあるモジュールをimportするときの注意点
# http://d.hatena.ne.jp/chlere/20110618/1308369842

# ユーザ一覧
class HelloListView(ListView):
    model = Friend
    template_name = 'hello/index.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー一覧画面"
        return context

#    def get_queryset(self):
#        object_list = self.model.objects.all().order_by('id')
#        q_friend= self.request.GET.get('friend')
#        if q_friend is not None:
#            if q_friend != "":
#                object_list = object_list.filter(friend=q_friend)
#        return object_list

# ユーザ登録
class HelloCreateView(CreateView):
    model = Friend
    form_class = FriendForm
    template_name = "hello/create.html"
    success_url = "/hello"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー登録画面"
        return context

# ユーザ詳細
class HelloDetailView(DetailView):
    model = Friend
    form_class = FriendForm
    template_name = "hello/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー詳細画面"
        return context

# ユーザ編集
class HelloUpdateView(UpdateView):
    model = Friend
    form_class = FriendForm
    template_name = 'hello/update.html'
    success_url = "/hello"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー編集画面"
        return context

# ユーザ削除
class HelloDeleteView(DeleteView):
    model = Friend
    form_class = FriendForm
    template_name = 'hello/delete.html'
    success_url = "/hello"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー削除画面"
        return context

#　メッセージ一覧
class MessageListView(ListView):
    model = Message
    template_name = 'hello/message.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "メッセージ一覧画面"
        return context

# メッセージ登録
class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'hello/message.html'
    success_url = "/hello"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "メッセージ登録画面"
        return context

# メッセージ詳細
class MessageDetailView(DetailView):
    model = Message
    form_class = MessageForm
    template_name = 'hello/message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "メッセージ詳細画面"
        return context

class HelloPdfListView(ListView):
    model = Friend
    template_name = 'hello/index.html'

    def render_to_response(self, context):
        html = get_template(self.template_name).render(self.get_context_data())
        result = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode('utf-8')),
            result,
            link_callback=link_callback,
            encoding='utf-8',
        )

        if not pdf.err:
            return HttpResponse(
                result.getvalue(),
                content_type='application/pdf'
            )

        return HttpResponse('<pre>%s</pre>' % escape(html))

def link_callback(uri, rel):
    path = os.path.join(settings.BASE_DIR, 'common', 'static/pdf')

    if not os.path.isfile(path):
        raise Exception(path)

    return path

def HelloPdf(request):
    # 源真ゴシック（ http://jikasei.me/font/genshin/）
    ttf = os.path.join(settings.BASE_DIR, 'common', 'static/fonts/MS Gothic.ttf')
    
    # 白紙をつくる（A4縦）
    FILENAME = 'HelloWorld.pdf'
    c = canvas.Canvas(FILENAME, pagesize=portrait(A4))
    
    # フォント登録
    pdfmetrics.registerFont(TTFont('font', ttf))
    font_size = 20
    c.setFont('font', font_size)
    
    # 真ん中に文字列描画
    width, height = A4  # A4用紙のサイズ
    c.drawCentredString(width / 2, height / 2 - font_size * 0.4, 'こんにちは、世界！')
    
    # Canvasに書き込み
    c.showPage()
    # ファイル保存
    c.save()
    
    # ブラウザーで表示
    webbrowser.open(FILENAME)