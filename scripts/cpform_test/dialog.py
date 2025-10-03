#!/usr/bin/python
# -*-coding:utf-8 -*-
# pylint: disable=duplicate-code
u"""
:创建时间: 2025/9/23 11:20
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:Github: https://github.com/cpcgskill
:QQ: 2921251087
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
:爱发电: https://afdian.net/@Phantom_of_the_Cang

"""
from __future__ import unicode_literals, print_function, division

# pylint: enable=duplicate-code

try:
    from PyQt6.QtWidgets import *
    from PyQt6.QtCore import *
    from PyQt6.QtGui import *

    gui_runtime = 'PyQt6'
except ImportError:
    try:
        from PySide6.QtGui import *
        from PySide6.QtCore import *
        from PySide6.QtWidgets import *

        gui_runtime = 'PySide6'
    except ImportError:
        try:
            from PyQt5.QtWidgets import *
            from PyQt5.QtCore import *
            from PyQt5.QtGui import *

            gui_runtime = 'PyQt5'
        except ImportError:
            try:
                from PySide2.QtGui import *
                from PySide2.QtCore import *
                from PySide2.QtWidgets import *

                gui_runtime = 'PySide2'
            except ImportError:
                from PySide.QtGui import *
                from PySide.QtCore import *

                gui_runtime = 'PySide'
import sys

app = QApplication(sys.argv)

try:
    import maya.standalone

    maya.standalone.initialize(name='python')
except:
    pass

from cpform.dialog import *


def show():
    print(
        'get_open_file_name',
        get_open_file_name()
    )
    print(
        'get_save_file_name',
        get_save_file_name()
    )
    print(
        'get_directory_name',
        get_directory_name()
    )
    print(
        'show_message',
        show_message(
            title='测试',
            message='这是一条测试消息, this is a test message, これはテストメッセージです, 이것은 테스트 메시지입니다.',
            icon='info',
        )
    )
    print(
        'show_confirm',
        show_confirm(
            title='确认',
            message='你确定要继续吗？, Are you sure you want to continue?, 続行してもよろしいですか？, 계속하시겠습니까?',
            icon='help-circle',
        )
    )
    print(
        'show_input',
        show_input(
            title='输入',
            message='请输入你的名字: , Please enter your name:, あなたの名前を入力してください:, 이름을 입력하세요:',
            placeholder_text='Your Name',
        )
    )
    print(
        'show_multi_line_input',
        show_multi_line_input(
            title='多行输入',
            message='请输入你的描述: , Please enter your description:, あなたの説明を入力してください:, 설명을 입력하세요:',
            placeholder_text='Your Description',
        )
    )
    print(
        'show_multi_input',
        show_multi_input(
            title='多输入',
            message='请输入你的信息: , Please enter your information:, あなたの情報を入力してください:, 정보를 입력하세요:',
            fields=[
                {'key': 'name', 'label': '名称(Name)', 'placeholder': 'Your Name'},
                {'key': 'age', 'label': '年龄(Age)', 'placeholder': 'Your Age'},
                {'key': 'email', 'label': '邮箱(Email)', 'placeholder': 'Your Email'},
            ]
        )
    )


show()
if sys.version_info.major == 2:
    exec('app.exec_()')
else:
    exec('app.exec_()')
