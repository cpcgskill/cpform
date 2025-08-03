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

import os

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

from cpform.widget.core import *
from cpform.widget.process import *
import cpform.docker as docker


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
        workdir=os.sep.join(os.path.abspath(__file__).split(os.sep)[:-3]),
        success_call=lambda code, stdout, stderr: print('success', code, stdout, stderr),
        fail_call=lambda code, stdout, stderr: print('fail', code, stdout, stderr),
    )
    # , '#fff799'
    docker.default_docker(title='radiant_joint_tool', form=Background(ui, '#354e6b'))


show()
if sys.version_info.major > 2:
    exec('app.exec()')
else:
    exec('app.exec_()')
