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

from imp import reload
import cpform

reload(cpform)

import cpform.item.core as item
import cpform.docker as docker

from maya_utils import call_block


@call_block
def call(*args, **kwargs):
    print(args, kwargs)


def radiant_joint_tool():
    return item.SubmitWidget(doit_text="选择羽毛关节", form=(
        item.Help(
            text="""十分艰苦拉萨艰苦拉萨附近可考虑十分艰苦拉萨艰苦拉萨附近可考虑十分艰苦拉萨艰苦拉萨附近可考虑十分艰苦拉萨艰苦拉萨附近可考虑十分艰苦拉萨艰苦拉萨附近可考虑"""
        ),
        item.FormLayout(
            childs=[
                "父控制器", item.Select(),
                "父控制器", item.Select(),
                "父控制器", item.Select(),
                "父控制器", item.Select(),
                "父控制器", item.IntSlider(2, 10, 3),
                "父控制器", item.IntSlider(2, 10, 5),
                "", item.Is(info="父控制器"),
            ]
        ),
    ), func=call)


def show():
    ui = item.ScrollArea(item.VBoxLayout(
        childs=[
            radiant_joint_tool(),
            radiant_joint_tool(),
        ]
    ))

    docker.logo_docker(title='radiant_joint_tool', form=ui)


show()
app.exec_()
