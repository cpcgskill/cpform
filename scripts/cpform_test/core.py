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

import cpmel

from imp import reload
import cpform

reload(cpform)

from cpform.item.all import *
import cpform.docker as docker

from maya_utils import call_block


@call_block
def call(*args, **kwargs):
    print(args, kwargs)


def radiant_joint_tool():
    return SubmitWidget(doit_text="选择羽毛关节", form=(
        Help(
            text="""十分艰苦拉萨艰苦拉萨附近可考虑十分艰苦拉萨艰苦拉萨附近可考虑十分艰苦拉萨艰苦拉萨附近可考虑十分艰苦拉萨艰苦拉萨附近可考虑十分艰苦拉萨艰苦拉萨附近可考虑"""
        ),
        FormLayout(
            childs=[
                "父控制器", LineEdit(text='', placeholder_text='父控制器'),
                "父控制器", Select(text='', placeholder_text='父控制器'),
                "父控制器", SelectList(text='', placeholder_text='父控制器'),
                "父控制器", Select(),
                "父控制器", Select(),
                "父控制器", Select(),
                "父控制器", IntSlider(2, 10, 3),
                "父控制器", IntSlider(2, 10, 5),
                "父控制器", FloatSlider(2, 10, 5),
                "", Background(CheckBox(info="父控制器"), '#b0333d'),
            ]
        ),
    ), func=call)


def show():
    ui = ScrollArea(VBoxLayout(
        childs=[
            Collapse(radiant_joint_tool(), text='radiant_joint_tool', default_state=True),
            Collapse(radiant_joint_tool(), text='radiant_joint_tool'),
        ],
        align='top'
    ))

    docker.logo_docker(title='radiant_joint_tool', form=ui)


show()
app.exec_()
