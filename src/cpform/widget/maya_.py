# -*-coding:utf-8 -*-
"""
:创建时间: 2022/7/10 3:29
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:Github: https://github.com/cpcgskill
:QQ: 2921251087
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
:爱发电: https://afdian.net/@Phantom_of_the_Cang

"""
from __future__ import unicode_literals, print_function, division

import maya.cmds as mc
from maya_utils import decode_string, call_block

from cpform.exc import CPMelFormException
from cpform.widget.core import *

__all__ = ['Select', 'SelectList']


class Select(Warp):
    def __init__(self, *args, **kwargs):
        self.line_edit = LineEdit(*args, **kwargs)
        self.load_bn = Button('载入', lambda *args: self.load())
        super(Select, self).__init__(HBoxLayout(childs=[self.line_edit, self.load_bn], margins=0, spacing=5))

    @call_block
    def load(self):
        sel = mc.ls(sl=True)
        if len(sel) < 1:
            raise CPMelFormException("选择一个物体")
        self.line_edit.set_text(sel[0])

    def read_data(self):
        return self.line_edit.read_data()


class SelectList(Warp):
    def __init__(self, *args, **kwargs):
        self.line_edit = LineEdit(*args, **kwargs)
        self.load_bn = Button('载入', lambda *args: self.load())
        super(SelectList, self).__init__(HBoxLayout(childs=[self.line_edit, self.load_bn], margins=0, spacing=5))

    @call_block
    def load(self):
        sel = mc.ls(sl=True)
        self.line_edit.set_text(u";".join(sel))

    def read_data(self):
        return self.line_edit.read_data()[0].split(";")
