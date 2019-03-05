# -*- coding: utf-8 -*-

import os
from io import BytesIO
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


class Render:

    @staticmethod
    def render(path: str, params: dict):
        print ('********** pdf 作成開始 **********')

        print ('settings.STATICFILES_DIRS:' + settings.STATICFILES_DIRS[0])

        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(
                BytesIO(html.encode('utf-8')),
                response,
                link_callback=link_callback,
                encoding='utf-8')

        if not pdf.err:
            print ('********** pdfの作成に成功しました **********')
            # return HttpResponse(response.getvalue(), content_type='application/pdf')
            return HttpResponse('<pre>%s</pre>' % escape(html))

        else:
            print ('********** pdfの作成に失敗しました　err:{{pdf.err}} **********')
            return HttpResponse("Error Rendering PDF", status=400)

def link_callback(uri, rel):
    return settings.STATICFILES_DIRS[0]
