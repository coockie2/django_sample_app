# -*- coding: utf-8 -*-
import datetime

from reportlab.lib.pagesizes import A4

from common.utils.pdf.base_render import BaseRender

class SampleRender(BaseRender):

    # pdfのファイル名
    def filename(self):
        return 'HelloWorld_{0:%Y%m%d%H%M%S}.pdf'.format(datetime.datetime.now())

    # pdfに出力する内容
    def draw(self):
        # 真ん中に文字列描画
        width, height = A4  # A4用紙のサイズ
        self.c.drawCentredString(width / 2, height / 2 - self.font_size * 0.4, 'こんにちは、世界！')
