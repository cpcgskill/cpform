#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/11/9 11:07
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function, division
import os
import sys

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

try:
    from shiboken2 import *
except ImportError:
    from shiboken import *

import maya.OpenMayaUI as OpenMayaUI
import maya.cmds as mc

try:
    if hasattr(mc, "about"):
        ptr_t = int if sys.version_info.major > 2 else long
        mui = wrapInstance(ptr_t(OpenMayaUI.MQtUtil.mainWindow()), QWidget)
    else:
        mui = None
except:
    mui = None

from cpform.widget.core import ToggleWidget, WarpWidget
from cpform.exc import CPMelFormException

PATH = os.path.dirname(os.path.abspath(__file__))
ICON = os.sep.join([PATH, u"icon.png"])
QSS = os.sep.join([PATH, u"qss.css"])
HEAD = os.sep.join([PATH, u"head.png"])
FONT = os.sep.join([PATH, u"NotoSansHans-Black.otf"])
with open(QSS, "rb") as f:
    QSS_STRING = f.read().decode('utf-8')


class Head(WarpWidget):
    def __init__(self):
        head_label = QLabel()
        pix = QPixmap(HEAD)
        head_label.setPixmap(pix)

        super(Head, self).__init__(
            child=head_label,
            left_clicked_callback=lambda *args: QDesktopServices.openUrl(QUrl(u'https://www.cpcgskill.com')),
            fixed_width=pix.width(),
            fixed_height=pix.height(),
        )


class BaseDocker(QWidget):
    def __init__(self, form, parent=None):
        super(BaseDocker, self).__init__(parent)
        self.setStyleSheet(QSS_STRING)
        id_ = QFontDatabase.addApplicationFont(FONT)
        QFontDatabase.applicationFontFamilies(id_)

        self.toggle = ToggleWidget(form)


class WidgetDocker(BaseDocker):
    def __init__(self, form=tuple(), parent=None):
        super(WidgetDocker, self).__init__(form, parent)

        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)

        self._main_layout.addWidget(self.toggle)


class WindowDocker(BaseDocker):
    def __init__(self, form=tuple(), icon=None, title=u"CPWindow"):
        if icon is None:
            icon = ICON
        super(WindowDocker, self).__init__(form, mui)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))

    def set_form(self, icon, title, form):
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self.toggle.toggle_to(form)

    def paintEvent(self, *args):
        p = QPainter(self)
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(QColor("#444444")))
        p.drawRect(self.rect())
        p.end()


class LogoDocker(WindowDocker):
    def __init__(self, icon=None,
                 title=u"CPWindow",
                 form=tuple()):
        super(LogoDocker, self).__init__(form, icon, title)

        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(2)

        self._head_widget = Head()

        self._main_layout.addWidget(self._head_widget)
        self._main_layout.addWidget(self.toggle)

    def set_form(self, icon, title, form):
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self.toggle.toggle_to(form)


class MiddleDocker(WindowDocker):
    def __init__(self, icon=None,
                 title=u"CPWindow",
                 form=tuple()):
        super(MiddleDocker, self).__init__(form, icon, title)

        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(*([20] * 4))
        self._main_layout.setSpacing(0)

        self._v_layout = QHBoxLayout()
        self._v_layout.setContentsMargins(0, 0, 0, 0)
        self._v_layout.setSpacing(0)

        self._h_layout = QHBoxLayout()
        self._h_layout.setContentsMargins(0, 0, 0, 0)
        self._h_layout.setSpacing(0)

        self._h_layout.addStretch(0)
        self._main_layout.addWidget(self.toggle)
        self._h_layout.addStretch(0)

        self._v_layout.addStretch(0)
        self._v_layout.addLayout(self._h_layout)
        self._v_layout.addStretch(0)

        self._main_layout.addStretch(0)
        self._main_layout.addLayout(self._v_layout)
        self._main_layout.addStretch(0)

    def set_form(self, icon, title, form):
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self.toggle.toggle_to(form)


class DefaultDocker(WindowDocker):
    def __init__(self, icon=None,
                 title=u"CPWindow",
                 form=tuple()):
        super(DefaultDocker, self).__init__(form, icon, title)

        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)

        self.toggle = ToggleWidget(form)

        self._main_layout.addWidget(self.toggle)

    def set_form(self, icon, title, form):
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self.toggle.toggle_to(form)


docker_table = dict()


def get_docker(name, default=None):
    return docker_table.get(name, default)


def close_docker(name="CPWindow"):
    widget = docker_table.get(name, None)
    if widget is None:
        raise CPMelFormException('容器不存在')
    widget.close()


def delete_docker(name="CPWindow"):
    widget = docker_table.get(name, None)
    if widget is None:
        raise CPMelFormException('容器不存在')
    widget.close()
    widget.deleteLater()
    docker_table.pop(name)


def widget_docker(form=tuple(), parent=None):
    u"""
    build函数提供将表单(列表 or 元组)编译为界面的功能

    :param form: 表单
    :param parent:
    :return:
    """
    return WidgetDocker(form, parent)


def default_docker(icon=None, name="CPWindow", title=None, form=tuple()):
    u"""
    build函数提供将表单(列表 or 元组)编译为界面的功能

    :param name:
    :param icon: 图标路径
    :param title: 标题
    :param form: 表单
    :return:
    """
    if title is None:
        title = name
    if name in docker_table:
        widget = docker_table[name]
        widget.set_form(icon, title, form)
    else:
        widget = DefaultDocker(icon, title, form)
    if not widget.isVisible():
        widget.show()
    docker_table[name] = widget


def logo_docker(icon=None, name="CPWindow", title=None, form=tuple()):
    u"""
    build函数提供将表单(列表 or 元组)编译为界面的功能

    :param name:
    :param icon: 图标路径
    :param title: 标题
    :param form: 表单
    :return:
    """
    if title is None:
        title = name
    if name in docker_table:
        widget = docker_table[name]
        widget.set_form(icon, title, form)
    else:
        widget = LogoDocker(icon, title, form)
    if not widget.isVisible():
        widget.show()
    docker_table[name] = widget


def middle_docker(icon=None, name="CPWindow", title=None, form=tuple()):
    u"""
    build函数提供将表单(列表 or 元组)编译为界面的功能

    :param name:
    :param icon: 图标路径
    :param title: 标题
    :param form: 表单
    :return:
    """
    if title is None:
        title = name
    if name in docker_table:
        widget = docker_table[name]
        widget.set_form(icon, title, form)
    else:
        widget = MiddleDocker(icon, title, form)
    if not widget.isVisible():
        widget.show()
    docker_table[name] = widget
