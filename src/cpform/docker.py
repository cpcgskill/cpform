#!/usr/bin/python
# -*-coding:utf-8 -*-
"""
:创建时间: 2020/11/9 11:07
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function, division

if False:
    from typing import *

import os
import sys

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

import cpform.utils as _cpform_utils
if _cpform_utils.runtime() == 'maya':
    try:
        from shiboken6 import *
    except ImportError:
        try:
            from shiboken2 import *
        except ImportError:
            from shiboken import *

    import maya.OpenMayaUI as OpenMayaUI
    import maya.cmds as mc

    try:
        if hasattr(mc, 'about'):
            ptr_t = int if sys.version_info.major > 2 else long
            mui = wrapInstance(ptr_t(OpenMayaUI.MQtUtil.mainWindow()), QWidget)
        else:
            mui = None
    except:
        mui = None
elif _cpform_utils.runtime() == '3dsMax':
    try:
        import qtmax
        mui = qtmax.GetQMaxMainWindow()
    except ImportError:
        try:
            from pymxs import runtime as rt
        except ImportError:
            mui = None
        else:
            if QWidget.find(rt.windows.getMAXHWND()):
                mui =  QMainWindow.find(rt.windows.getMAXHWND())
            else:
                mui = None
else:
    mui = None

import cpform.config as cf_config
from cpform.utils import call_block
from cpform.widget.core import ToggleWidget, WarpWidget, BackgroundWidget, VBoxLayout, Widget
from cpform.exc import CPMelFormException

PATH = os.path.dirname(os.path.abspath(__file__))
QSS = os.sep.join([PATH, 'assets', 'qss.css'])
HEAD = os.sep.join([PATH, 'assets', 'head.png'])
FONT_DIR = os.sep.join([PATH, 'assets', 'fonts'])
with open(QSS, "rb") as f:
    QSS_STRING = f.read().decode('utf-8')


def _read_qss_string():
    qss_str = QSS_STRING
    qss_str = qss_str.replace(
        '{{RoundCorners}}',
        '{}px;'.format(cf_config.RoundCornersLevel3)
    )
    qss_str = qss_str.replace(
        '{{RoundCornersLevel3}}',
        '{}px;'.format(cf_config.RoundCornersLevel3)
    )
    qss_str = qss_str.replace(
        '{{RoundCornersLevel2}}',
        '{}px;'.format(cf_config.RoundCornersLevel2)
    )
    qss_str = qss_str.replace(
        '{{RoundCornersLevel1}}',
        '{}px;'.format(cf_config.RoundCornersLevel1)
    )
    qss_str = qss_str.replace(
        '{{AttentionColor}}',
        cf_config.AttentionColor,
    )
    qss_str = qss_str.replace(
        '{{LineWidth}}',
        '{}px'.format(cf_config.LineWidth),
    )
    qss_str = qss_str.replace(
        '{{LineColor}}',
        '{}'.format(cf_config.LineColor),
    )
    qss_str = qss_str.replace(
        '{{LightOverlayRgbaColor}}',
        'rgba(255, 255, 255, {})'.format(int(round(255 * cf_config.LightOverlayColorChange))),
    )
    qss_str = qss_str.replace(
        '{{DarkOverlayRgbaColor}}',
        'rgba(0, 0, 0, {})'.format(int(round(255 * cf_config.DarkOverlayColorChange))),
    )
    qss_str = qss_str.replace(
        '{{Height}}',
        '{}px'.format(cf_config.Height),
    )
    qss_str = qss_str.replace(
        '{{Height*2}}',
        '{}px'.format(cf_config.Height * 2),
    )
    qss_str = qss_str.replace(
        '{{Padding}}',
        '{}px'.format(cf_config.Padding),
    )
    qss_str = qss_str.replace(
        '{{FontSize}}',
        '{}px'.format(cf_config.FontSize),
    )
    qss_str = qss_str.replace(
        '{{FontFamily}}',
        '"{}", "Microsoft YaHei"'.format(cf_config.Font, "Microsoft YaHei"),
    )
    return qss_str


def _initialization_Widget(widget):
    widget.setStyleSheet(_read_qss_string())
    for root, dirs, files in os.walk(FONT_DIR):
        for file in files:
            if file.endswith('.otf') or file.endswith('.ttf'):
                id_ = QFontDatabase.addApplicationFont(os.path.join(root, file))
                QFontDatabase.applicationFontFamilies(id_)


class DockerWarp(object):
    def __init__(self, delete_callback):
        self._delete_callback = delete_callback

    def delete_docker(self):
        self._delete_callback()
        return self


class DialogDocker(QDialog):
    def __init__(self, form, icon=None, title='CPWindow'):
        """

        :type form: Widget
        :type icon: AnyStr
        :type title: AnyStr
        """
        if icon is None:
            icon = cf_config.DefaultIcon
        super(DialogDocker, self).__init__(mui)
        _initialization_Widget(self)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))

        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)

        self.toggle = ToggleWidget(BackgroundWidget(form, color='#444444'))

        self._main_layout.addWidget(self.toggle)


class PopupMenuDocker(QDialog):
    def __init__(self, form, close_callback=None):
        """

        :type form: Widget
        """
        self._is_delete = False

        self._close_callback = None
        if callable(close_callback):
            self._close_callback = call_block(close_callback)

        super(PopupMenuDocker, self).__init__()
        _initialization_Widget(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)

        self._main_layout.addWidget(BackgroundWidget(form, color='#444444'))

    def showEvent(self, *args, **kwargs):
        self.setFocus()

        # 监测焦点变化并关闭菜单
        def _on_focus_changed(old, new):
            if not self._is_delete:
                if new is None or not self.isAncestorOf(new):
                    self.delete_popup_menu()

        QApplication.instance().focusChanged.connect(_on_focus_changed)

    def closeEvent(self, *args, **kwargs):
        if self._close_callback is not None:
            self._close_callback()

    def delete_popup_menu(self):
        if not self._is_delete:
            self.close()
            self.deleteLater()
            self._is_delete = True


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

    def read_data(self):
        return []


class BaseDocker(QWidget):
    def __init__(self, form, parent=None):
        super(BaseDocker, self).__init__(parent)
        _initialization_Widget(self)

        self.toggle = ToggleWidget(form)


class WidgetDocker(BaseDocker):
    def __init__(self, form=tuple(), parent=None):
        super(WidgetDocker, self).__init__(form, parent)

        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)

        self._main_layout.addWidget(self.toggle)


class WindowDocker(BaseDocker):
    def __init__(self, form=tuple(), icon=None, title=u"CPWindow", size=None):
        if icon is None:
            icon = cf_config.DefaultIcon
        super(WindowDocker, self).__init__(form, mui)
        self.setWindowFlags(Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        if size is not None:
            self.resize(QSize(*size))

    def set_form(self, icon, title, form, size):
        if icon is None:
            icon = cf_config.DefaultIcon
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self.toggle.toggle_to(form)
        if size is not None:
            self.resize(QSize(*size))

    def paintEvent(self, *args):
        p = QPainter(self)
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(QColor("#444444")))
        p.drawRect(self.rect())
        p.end()


class LogoDocker(WindowDocker):
    def __init__(self, icon=None,
                 title=u"CPWindow",
                 form=tuple(),
                 size=None):
        super(LogoDocker, self).__init__(form, icon, title, size)

        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(2)

        self._head_widget = Head()

        self._main_layout.addWidget(self._head_widget)
        self._main_layout.addWidget(self.toggle)

    def set_form(self, icon, title, form, size):
        if icon is None:
            icon = cf_config.DefaultIcon
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self.toggle.toggle_to(form)
        if size is not None:
            self.resize(QSize(*size))


class MiddleDocker(WindowDocker):
    def __init__(self, icon=None,
                 title=u"CPWindow",
                 form=tuple(),
                 size=None):
        super(MiddleDocker, self).__init__(form, icon, title, size)

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

    def set_form(self, icon, title, form, size):
        if icon is None:
            icon = cf_config.DefaultIcon
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self.toggle.toggle_to(form)
        if size is not None:
            self.resize(QSize(*size))


class DefaultDocker(WindowDocker):
    def __init__(self, icon=None,
                 title=u"CPWindow",
                 form=tuple(),
                 size=None):
        super(DefaultDocker, self).__init__(form, icon, title, size)

        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)

        self.toggle = ToggleWidget(form)

        self._main_layout.addWidget(self.toggle)

    def set_form(self, icon, title, form, size):
        if icon is None:
            icon = cf_config.DefaultIcon
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self.toggle.toggle_to(form)
        if size is not None:
            self.resize(QSize(*size))


_this_dialog = None  # type: DialogDocker or None


def dialog_docker(form, icon=None, title='CPWindow'):
    """
    build函数提供将表单(列表 or 元组)编译为界面的功能

    :type form: Widget
    :param form: 表单
    :param icon: 图标路径
    :param title: 标题
    :return:
    """
    global _this_dialog
    old_this_dialog = _this_dialog
    try:
        _this_dialog = DialogDocker(form, icon, title)
        _this_dialog.exec_()
        _this_dialog.close()
        _this_dialog.deleteLater()
        return _this_dialog
    finally:
        _this_dialog = old_this_dialog


def quit_dialog_docker():
    global _this_dialog
    if _this_dialog is not None:
        _this_dialog.close()


def popup_menu_docker(form, pos=None, from_widget=None, close_callback=None):
    widget = PopupMenuDocker(form, close_callback=close_callback)
    if pos is None:
        pos = QCursor().pos()
    widget.move(pos)
    if from_widget is not None:
        widget.move(from_widget.mapToGlobal(QPoint(0, from_widget.height())))
        widget.setFixedWidth(from_widget.width())
    widget.show()

    return DockerWarp(delete_callback=widget.delete_popup_menu)


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


def default_docker(icon=None, name="CPWindow", title=None, form=tuple(), size=None):
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
        widget.set_form(icon, title, form, size)
    else:
        widget = DefaultDocker(icon, title, form, size)
    if not widget.isVisible():
        widget.show()
    docker_table[name] = widget


def logo_docker(icon=None, name="CPWindow", title=None, form=tuple(), size=None):
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
        widget.set_form(icon, title, form, size)
    else:
        widget = LogoDocker(icon, title, form, size)
    if not widget.isVisible():
        widget.show()
    docker_table[name] = widget


def middle_docker(icon=None, name="CPWindow", title=None, form=tuple(), size=None):
    u"""
    build函数提供将表单(列表 or 元组)编译为界面的功能

    :param name:
    :param icon: 图标路径
    :param title: 标题
    :param form: 表单
    :return:
    """
    form = VBoxLayout(
        childs=[Head(), form]
    )
    default_docker(form, icon, name, title, size)
