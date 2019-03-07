# -*- coding: utf-8 -*-
import win32com.client
 
import os.path
import os
import pythoncom
import webbrowser

from django.conf import settings

# [PYTHON] EXCELのシートをJPEGに書き出す [EXCEL]
# http://flame-blaze.net/archives/7014
class excelToPdf:

    @classmethod
    def export(self):
        self.file_path = os.path.join(settings.BASE_DIR, 'common', 'static/excel/test.xlsx')
        self.to_path = os.path.join(settings.BASE_DIR, 'common', 'static/pdf/test.pdf')

        pythoncom.CoInitializeEx(pythoncom.COINIT_MULTITHREADED)
        self.o = win32com.client.Dispatch("Excel.Application")
        # Excel起動しない
        self.o.Visible = False
        # エラー表示しない
        self.o.DisplayAlerts = False

        self.wb = self.o.Workbooks.Open(self.file_path)

        #off-by-one so the user can start numbering the worksheets at 1
        self.ws = self.wb.Worksheets[0]
        # 倍率は指定しない
        self.ws.PageSetup.Zoom = False
        # http://www.moug.net/tech/exvba/0070009.html
        # 縦方向1ページで印刷
        self.ws.PageSetup.FitToPagesTall = 1
        # 横方向1ページで印刷
        self.ws.PageSetup.FitToPagesWide = 1
        self.ws.PageSetup.PrintArea = "A1:C36"
    
        self.wb.WorkSheets([1,2]).Select()
        self.wb.ActiveSheet.ExportAsFixedFormat(0, self.to_path)

        self.wb.Close(False)

        # ブラウザーで表示
        webbrowser.open(self.to_path)
