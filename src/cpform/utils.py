# -*-coding:utf-8 -*-
"""
:创建时间: 2022/8/1 23:41
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:Github: https://github.com/cpcgskill
:QQ: 2921251087
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
:爱发电: https://afdian.net/@Phantom_of_the_Cang

"""
from __future__ import unicode_literals, print_function, division
import maya_utils
from maya_utils import decode_string
import maya.cmds as mc

__all__ = ['call_block', 'decode_string', 'runtime', 'runtime_version']


def call_block(fn):
    return maya_utils.execute_deferred(maya_utils.call_block(fn))


def runtime():
    return 'maya'


def runtime_version():
    return int(eval(mc.about(lu=True))[1])
