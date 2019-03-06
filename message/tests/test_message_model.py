# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import TestCase

from django.core.exceptions import ValidationError

from message.models import Message

# アサート専用クラス
class MessageAssertion(TestCase):
    def assertMessageModel(self, message, content):
        self.assertEqual(message.content, content)

# Messageモデルをテスト
class MessageModelTests(TestCase):
    def creating_a_book_and_saving(self, content=None):
        message = Message()
        if content is not None:
            message.content = content
        message.owner = self.user
        message.save()

    @classmethod
    def setUpTestData(cls):
        print ('setUpTestData start!!')

    def setUp(self):
        self.user = User.objects.create_user('tester')

    # Messageのレコード数は0件
    def test_is_empty(self):
        self.assertEqual(Message.objects.all().count(), 0)

    # Messageのレコード数は1件
    def test_is_not_empty(self):
        self.creating_a_book_and_saving('test message')
        self.assertEqual(Message.objects.all().count(), 1)

    # 指定した内容が保存されているか
    def test_saving_and_retrieving_book(self):
        content = 'test message'
        self.creating_a_book_and_saving(content)
        self.assertEqual(Message.objects.all()[0].content, content)

    # contentが空のデータは保存できない
    def test_is_content_empty_is_error(self):
        self.assertRaises(ValidationError, lambda: Message().full_clean())

    # contentが201文字以上のデータは保存できない
    def test_is_content_200_over_is_error(self):
        message = Message()
        message.content = ('0123456789' * 20) + '0'
        self.assertRaises(ValidationError, lambda: message.full_clean())

    def tearDown(self):
        self.user.delete()
