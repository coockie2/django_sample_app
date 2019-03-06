# coding:utf-8
import io
from PIL import Image

from django.shortcuts import render

# 下記のサイトを参考に一部書き換え
# Djangoにmatplotlibで円グラフ表示
# https://qiita.com/tfuruya/items/f9de3039ad2d60b09c7b
def index(request):
    return render(request, 'graph/index.html', {})

def simple(request):
    import django
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    import matplotlib.pyplot as plt

    # matpotlib 用データの定義
    datas = [20, 30, 10]
    labels = ['Wine', 'Sake', 'Beer']
    colors = ['yellow', 'red', 'green']

    # matplotlibを使用してグラフを作成
    fig = plt.figure(1,figsize=(4,4))
    ax = fig.add_subplot(111) 
    ax.axis("equal")
    pie = ax.pie(datas, #データ
                 startangle=90, #円グラフ開始軸を指定
                 labels=labels, #ラベル
                 autopct="%1.1f%%",#パーセント表示
                 colors=colors, #色指定
                 counterclock=False, #逆時計回り
                 )

    # canvasのデータをバイトデータ化
    buf = io.BytesIO()
    canvas=FigureCanvas(fig)
    canvas.print_png(buf)

    # バイトデータ化したデータをimage化 -> responseに付与
    response = django.http.HttpResponse(content_type='image/png')
    Image.open(buf).save(response, 'png')
    return response