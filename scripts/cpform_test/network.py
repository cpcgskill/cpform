# -*-coding:utf-8 -*-
"""
:创建时间: 2022/7/28 0:23
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:Github: https://github.com/cpcgskill
:QQ: 2921251087
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
:爱发电: https://afdian.net/@Phantom_of_the_Cang

"""
from __future__ import unicode_literals, print_function, division

import json

try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
except ImportError:
    try:
        from PySide2.QtGui import *
        from PySide2.QtCore import *
        from PySide2.QtWidgets import *
    except ImportError:
        from PySide.QtGui import *
        from PySide.QtCore import *
import sys

app = QApplication(sys.argv)

try:
    import maya.standalone

    maya.standalone.initialize(name='python')
except:
    pass

from cpform.widget.core import *
from cpform.widget.network import *
import cpform.docker as docker

from maya_utils import call_block


@call_block
def call(*args, **kwargs):
    print(args, kwargs)


def show():
    # ui = Process(
    #     child=QLabel('Test'),
    #     command='E:\\backup_to_cloud\\dev\\python_for_maya\\tool\\CGAssistant-client\\src\\cgass\\execs\\execs\\cgass.exe',
    #     args=['--help'],
    # )
    ui = VBoxLayout(
        childs=[
            # HttpGet(
            #     child=Label('Test'),
            #     url='https://assets-1301463658.file.myqcloud.com/news/html/CG-assistant-v-1-0-0.html',
            #     body='{张隆鑫}',
            # ),
            # HttpGet(
            #     child=Label('Test'),
            #     url='https://assets-1301463658.file.myqcloud.com/不存在这个文件.html',
            #     body='{张隆鑫}',
            # ),
            HttpGet(
                child=Label('Test'),
                url='https://assets-1301463658.cos.ap-hongkong.myqcloud.com/test/2022-09-16.mp4',
                success_call=lambda code, headers, body: print('big file download test success', code, headers, len(body)),
                fail_call=lambda err: print('big file download test fail', err),
            ),
            HttpPost(
                child=Label('Test'),
                url='https://bpnet.fun/user/v1/data',
                headers={'Content-Type': 'application/json'},
                body=json.dumps(
                    {
                        'jwt':
                            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLTEzMDE0NjM2NTguY29zLmFjY2VsZXJhdGUubXlxY2xvdWQuY29tL3VzZXIvaW1hZ2VzL2F2YXRhci8wMTE1YmZmNGUyYWU0YzA2YWZiNDE4ZDU0YzAxZjZlOC5wbmciLCJjcmVhdGVfdGltZSI6IjIwMjItMDQtMjdUMDE6NTM6MDFaIiwiZW1haWwiOiJkZXRpdGF3NDk5QHBhbnRhYmkuY29tIiwibmFtZSI6IuWViuWViuWViiIsInV1aWQiOiJjNTYyYTZiYy1jNWNjLTExZWMtYTJkYi0wMjQyYWMxMTAwMDcifSwiZXhwIjoxNjU5MDQ1NzMzLCJpYXQiOjE2NTg5NTkzMzMsInRva2VuX3R5cGUiOiJ1c2VyX2xvZ2luOnYyIiwidXVpZCI6ImM1NjJhNmJjLWM1Y2MtMTFlYy1hMmRiLTAyNDJhYzExMDAwNyJ9.I8LZvsHfi8qW-A-61m6AyUzYpF4rOmyeVpwdGGy1wow'
                    }
                ),
                success_call=lambda status_code, headers, body: print('post request test success', status_code, headers, body, body),
                fail_call=lambda error: print('post request test fail', error),
            ),
        ]
    )
    # , '#fff799'
    docker.default_docker(title='radiant_joint_tool', form=Background(ui, '#354e6b'))


show()
app.exec_()
