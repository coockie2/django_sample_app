# -*- coding: utf-8 -*-
from django import forms
from .models import Friend, Message

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']

    def __init__(self, *args, **kwargs):
        super(FriendForm, self).__init__(*args, **kwargs)
        print(self.fields)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class FindForm(forms.Form):
    find = forms.CharField(label = 'find', required = False)

class CheckForm(forms.Form):
    str = forms.CharField(label = 'String')

    # バリデーションエラー発生時にエラーメッセージを指定
#    def clean(self):
#        cleaned_data = super().clean()
#        str = cleaned_data['str']
#        if (str.lower().startswith('no')):
#            raise forms.ValidationError('You input "NO"!')

    # 文字列のバリデーション
    # empty = forms.CharField(label = 'Empty', empty_value = True)
    # min_length = forms.CharField(label = 'Min', min_length = 10)
    # max_length = forms.CharField(label = 'Max', max_length = 10)

    # 数値のバリデーション
    # required = forms.IntegerField(label = 'Required')
    # min_value = forms.IntegerField(label = 'Min', min_value = 100)
    # max_value = forms.IntegerField(label = 'Max', max_value = 1000)

    # 日付のバリデーション
    # date = forms.DateField(label = 'Date', input_formats=['%d'])
    # time = forms.TimeField(label = 'Time')
    # datetime = forms.DateTimeField(label = 'DateTime')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'friend']
