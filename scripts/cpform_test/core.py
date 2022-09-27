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

from cpform._lib.maya_utils import call_block


@call_block
def call(*args, **kwargs):
    print(args, kwargs)


def test_DataSetWidget():
    ui = VBoxLayout(childs=[
        LineEditWidget(text='Test', placeholder_text='Test'),
        DataSetWidget(VBoxLayout(childs=[
            LineEditWidget(text='Test', placeholder_text='Test'),
            LineEditWidget(text='Test', placeholder_text='Test'),
            LineEditWidget(text='Test', placeholder_text='Test'),
        ])),
        LineEditWidget(text='Test', placeholder_text='Test'),
        ButtonWidget(text='print data', func=lambda *args: print(list(ui.read_data()))),
    ])
    return ui


def radiant_joint_tool():
    return SubmitWidget(doit_text="选择羽毛关节", form=[
        LabelWidget('Test'),
        LabelWidget('Test', font_size=24),
        ButtonWidget('Test'),
        ButtonWidget('Test', icon='anchor'),
        ButtonWidget('', icon='anchor'),
        ButtonWidget('', icon='anchor', icon_size=30),
        ButtonWidget('', icon='anchor', icon_size=60),
        HeadLineWidget('Test', 1),
        HeadLineWidget('Test', 2),
        HeadLineWidget('Test', 3),
        HeadLineWidget('Test', 4),
        HeadLineWidget('Test', 5),
        HeadLineWidget('Test', 6),
        LineEditWidget(text='Test', placeholder_text='Test'),
        IntSliderWidget(2, 10, 3),
        FloatSliderWidget(2, 10, 5),
        CheckBoxWidget(info="Test"),
        BackgroundWidget(CheckBoxWidget(info="Test"), '#b0333d'),
        HelpWidget("TestTest TestTest TestTest TestTest TestTest TestTest"),
        test_DataSetWidget(),
        HeadLineWidget(
            text='widget call test',
            left_clicked_callback=lambda *args: print('widget call success(left_clicked_callback)'),
            right_clicked_callback=lambda *args: print('widget call success(right_clicked_callback)'),
        )
    ], func=call)


def show():
    ui = ScrollArea(VBoxLayout(
        childs=[
            Collapse(radiant_joint_tool(), text='Test', default_state=True),
            Collapse(radiant_joint_tool(), text='Test'),
        ],
        align='top'
    ))
    docker.default_docker(title='Test', form=BackgroundWidget(ui, '#354e6b'))


show()
app.exec_()
