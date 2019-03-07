# -*- coding: utf-8 -*-

import os
import logging
from .base import *

# Database
# https://docs.djangoproject.com/ja/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Djangoのコンソールにデバッグのメッセージを出力する方法
# https://qiita.com/NoriakiOshita/items/7716c6e46338768467eb
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)

# for email debug settings
# メール送信せずにログ出力に絞る設定
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
