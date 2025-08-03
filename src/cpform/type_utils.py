# -*-coding:utf-8 -*-
"""
:PROJECT_NAME: cpform
:File: type_utils.py
:Time: 2024/10/18 15:12
:Author: 张隆鑫
"""
from __future__ import unicode_literals, print_function, division

if False:
    from typing import *
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

UnicodeStrType = type('')
AnyStrType = (bytes, UnicodeStrType)
ColorType = QColor

AlignType = (AnyStrType, Qt.AlignmentFlag)

_align_map = {
    'left': Qt.AlignLeft,
    'right': Qt.AlignRight,
    'top': Qt.AlignTop,
    'bottom': Qt.AlignBottom,
    'center': Qt.AlignCenter,
}


def _to_native_align(align):
    if isinstance(align, Qt.AlignmentFlag):
        return align
    if align not in _align_map:
        raise ValueError('Unknown align: {}'.format(align))
    return _align_map[align]


SizePolicyType = (AnyStrType, QSizePolicy.Policy)

_size_policy_map = {
    'fixed': QSizePolicy.Policy.Fixed,
    'minimum': QSizePolicy.Policy.Minimum,
    'maximum': QSizePolicy.Policy.Maximum,
    'preferred': QSizePolicy.Policy.Preferred,
    'expanding': QSizePolicy.Policy.Expanding,
    'minimum_expanding': QSizePolicy.Policy.MinimumExpanding,
    'ignored': QSizePolicy.Policy.Ignored,
}


def _to_native_size_policy(policy):
    if isinstance(policy, QSizePolicy.Policy):
        return policy
    if policy not in _size_policy_map:
        raise ValueError('Unknown size policy: {}'.format(policy))
    return _size_policy_map[policy]


def new_color(color):
    """
    :type color: str|(int, int, int)|(int, int, int, int)
    :rtype: ColorType
    """
    if isinstance(color, AnyStrType):
        return QColor(color)
    else:
        return QColor(*color)


def rgb(r, g, b):
    return r, g, b


def rgba(r, g, b, a):
    return r, g, b, a
