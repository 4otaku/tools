# -*- coding: utf8 -*-
# License avaiavle at zalivator_license.txt in "licenses" directory

from lib.window.text import Window_Text

# ======================================================================
class Window_About(Window_Text):

    text = 'О программе.<br /><br />' + \
        'Данная небольшая программа предназначена для добавления ' + \
        'материалов на сайт <a href="http://4otaku.ru">http://4otaku.ru</a>.<br /><br />' + \
        'Версия программы 1.0.0b<br /><br />' + \
        'Написана она с использованием следующих технологий:<br />' + \
        'Язык программирования Python (распостраняется под лицензией PSFL)<br />' + \
        'Фреймворк для кроссплатформенной разработки QT (распостраняется под лицензией LGPL)<br />' + \
        'Библиотека PyQT (распостраняется под лицензией GNU GPL)<br />' + \
        'Спасибо их авторам за возможность бесплатного использования их работы.<br /><br />' + \
        'Сама программа "заливатор" также распостраняется под GNU GPL<br />' + \
        'Исходный код программы доступен по адресу ' + \
        '<a href="https://github.com/4otaku/tools/tree/master/zalivator/source">' + \
        'https://github.com/4otaku/tools/tree/master/zalivator/source</a><br />' + \
        'Все лицензии должны поставляться с программой, в папке "licenses"'

    def __init__(self, app):
        Window_Text.__init__(self, app)
