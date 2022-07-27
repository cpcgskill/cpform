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
            HttpRequest(
                child=Label('Test'),
                url='https://assets-1301463658.file.myqcloud.com/news/html/CG-assistant-v-1-0-0.html',
                method='GET',
                data='{张隆鑫}',
            ),
            HttpRequest(
                child=Label('Test'),
                url='https://assets-1301463658.file.myqcloud.com/news/html/CG-assistant-v-1-0-0.html',
                method='GET',
                data='{张隆鑫}',
            ),
            HttpRequest(
                child=Label('Test'),
                url='https://user-api.bpnet.fun/create_session_from_email',
                method='POST',
                headers={'Content-Type': 'application/json'},
                data='{"email": "2921251087@qq.com", "password": "asdfghjkl;\'"}',
            ),
        ]
    )
    # , '#fff799'
    docker.default_docker(title='radiant_joint_tool', form=Background(ui, '#354e6b'))


show()
app.exec_()
