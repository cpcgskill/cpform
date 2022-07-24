# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/4/22 3:46
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

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
import cpform.docker as docker

from maya_utils import call_block


@call_block
def call(*args, **kwargs):
    print(args, kwargs)


def test_DataSetWidget():
    ui = VBoxLayout(childs=[
        LineEdit(text='Test', placeholder_text='Test'),
        DataSetWidget(VBoxLayout(childs=[
            LineEdit(text='Test', placeholder_text='Test'),
            LineEdit(text='Test', placeholder_text='Test'),
            LineEdit(text='Test', placeholder_text='Test'),
        ])),
        LineEdit(text='Test', placeholder_text='Test'),
        Button(text='print data', func=lambda *args: print(list(ui.read_data()))),
    ])
    return ui


def radiant_joint_tool():
    return SubmitWidget(doit_text="选择羽毛关节", form=[
        Label('Test'),
        Label('Test', font_size=24),
        Button('Test'),
        Button('Test', icon='anchor'),
        Button('', icon='anchor'),
        Button('', icon='anchor', icon_size=30),
        Button('', icon='anchor', icon_size=60),
        HeadLine('Test', 1),
        HeadLine('Test', 2),
        HeadLine('Test', 3),
        HeadLine('Test', 4),
        HeadLine('Test', 5),
        HeadLine('Test', 6),
        LineEdit(text='Test', placeholder_text='Test'),
        IntSlider(2, 10, 3),
        FloatSlider(2, 10, 5),
        CheckBox(info="Test"),
        Background(CheckBox(info="Test"), '#b0333d'),
        Help("TestTest TestTest TestTest TestTest TestTest TestTest"),
        test_DataSetWidget(),
    ], func=call)


def show():
    ui = ScrollArea(VBoxLayout(
        childs=[
            Collapse(radiant_joint_tool(), text='radiant_joint_tool', default_state=True),
            Collapse(radiant_joint_tool(), text='radiant_joint_tool'),
        ],
        align='top'
    ))
    # , '#fff799'
    docker.default_docker(title='radiant_joint_tool', form=Background(ui, '#354e6b'))


show()
app.exec_()
