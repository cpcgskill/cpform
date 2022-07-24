# -*-coding:utf-8 -*-
"""
:创建时间: 2022/7/25 5:54
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
from cpform.widget.process import *
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
    ui = Process(
        child=Label('Test'),
        command='ls',
        workdir='E:\\backup_to_cloud\\dev\\python_for_maya\\package\\cpform',
        success_call=lambda code, stdout, stderr: print('success', code, stdout, stderr),
        fail_call=lambda code, stdout, stderr: print('fail', code, stdout, stderr),
    )
    # , '#fff799'
    docker.default_docker(title='radiant_joint_tool', form=Background(ui, '#354e6b'))


show()
app.exec_()
