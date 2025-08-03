#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/4/21 2:22
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function, division

import os
import re

try:
    from PyQt6.QtWidgets import *
    from PyQt6.QtCore import *
    from PyQt6.QtGui import *
    from PyQt6.QtSvgWidgets import QSvgWidget
except ImportError:
    try:
        from PySide6.QtGui import *
        from PySide6.QtCore import *
        from PySide6.QtWidgets import *
        from PySide6.QtSvgWidgets import QSvgWidget
    except ImportError:
        try:
            from PyQt5.QtWidgets import *
            from PyQt5.QtCore import *
            from PyQt5.QtGui import *
            from PyQt5.QtSvg import QSvgWidget
        except ImportError:
            try:
                from PySide2.QtGui import *
                from PySide2.QtCore import *
                from PySide2.QtWidgets import *
                from PySide2.QtSvg import QSvgWidget
            except ImportError:
                from PySide.QtGui import *
                from PySide.QtCore import *
                from PySide.QtSvg import QSvgWidget
path = [os.sep.join([os.path.dirname(os.path.abspath(__file__)), 'file'])]

_name_check = re.compile(r'^[a-zA-Z][a-zA-Z0-9_\-]*$')


def find_svg(name):
    """

    :type name: str|unicode
    :rtype: unicode
    """
    if _name_check.match(name):
        for root in path:
            file = ''.join([root, os.sep, name, '.svg'])
            if os.path.isfile(file):
                return file
        raise ValueError('not found svg file: %s' % name)
    else:
        if os.path.isfile(name):
            return name
        else:
            raise ValueError('not found svg file: %s' % name)


def widget(name):
    """
    :rtype: QSvgWidget
    """
    return QSvgWidget(find_svg(name))


def pixmap(name):
    """
    :rtype: QPixmap
    """
    return QPixmap(find_svg(name))


def image(name):
    """
    :rtype: QImage
    """
    return QImage(find_svg(name))
    # with open(find_svg(name), "rb") as f:
    #     return QImage.fromData(f.read())


def icon(name):
    """
    :rtype: QIcon
    """
    return QIcon(find_svg(name))
