# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/4/22 2:36
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function, division

import abc
from functools import partial

import cpmel.cmds as cc
from maya_utils import decode_string, call_block

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

from cpform.exc import CPMelFormException


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()

    def read_data(self):
        return []


class Help(Widget):
    def __init__(self, text=u""):
        text = decode_string(text)
        super(Help, self).__init__()
        self.setMinimumHeight(40)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        text = QLabel(text)
        text.setWordWrap(True)
        text.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(text)
        self.main_layout.addStretch(0)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(QColor(75, 75, 75)))
        p.drawRoundedRect(self.rect(), 4, 4)


class Label(Widget):
    def __init__(self, text=''):
        text = decode_string(text)
        super(Label, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(QLabel(text))


class HeadLine(Widget):
    def __init__(self, text='', level=1):
        text = decode_string(text)
        super(HeadLine, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)
        label.setObjectName('h{}'.format(level))
        self.main_layout.addWidget(label)


class LineEdit(Widget):
    def __init__(self, text=u"", is_encrypt=False):
        text = decode_string(text)
        super(LineEdit, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.text = QLineEdit(text)
        if is_encrypt:
            self.text.setEchoMode(QLineEdit.Password)
        self.main_layout.addWidget(self.text)

    def read_data(self):
        return [self.text.text()]


class Button(Widget):
    def __init__(self, text='', func=None):
        self.func = func
        text = decode_string(text)
        super(Button, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        bn = QPushButton(text)
        bn.clicked.connect(self.call)

        self.main_layout.addWidget(bn)

    def call(self):
        if self.func is not None:
            self.func()


class Select(Widget):
    def __init__(self):
        super(Select, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.text = QLineEdit()
        self.load_bn = QPushButton(u"载入")
        _ = partial(self.load)
        self.load_bn.clicked.connect(lambda *args: _())
        self.main_layout.addWidget(self.text)
        self.main_layout.addWidget(self.load_bn)

    @call_block
    def load(self):
        sel = cc.ls(sl=True)
        if len(sel) < 1:
            raise CPMelFormException("选择一个物体")
        self.text.setText(str(sel[0]))

    def read_data(self):
        return [self.text.text()]


class SelectList(Widget):
    def __init__(self):
        super(SelectList, self).__init__()
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.load_bn = QPushButton(u"载入")
        self.load_bn.clicked.connect(lambda *args: self.load())
        self.texts = QTextEdit()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.load_bn)
        layout.addStretch(0)

        self.main_layout.addLayout(layout)
        self.main_layout.addWidget(self.texts)

    @call_block
    def load(self):
        sel = cc.ls(sl=True)
        self.texts.setText(u"\n".join([str(i) for i in sel]))

    def read_data(self):
        return [self.texts.toPlainText().split("\n")]


class Is(Widget):
    def __init__(self, info=u"", default_state=False):
        info = decode_string(info)
        super(Is, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.query = QCheckBox(info, self)
        self.query.setChecked(default_state)
        self.main_layout.addWidget(self.query)

    def read_data(self):
        return [self.query.isChecked()]


class IntSlider(Widget):
    def __init__(self, min=0, max=100, def_=0):
        self.min = min
        self.max = max
        super(IntSlider, self).__init__()
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)

        self._text = QLineEdit()
        self._text.setFixedWidth(60)

        self._slider = QSlider(Qt.Horizontal, self)
        self._slider.setMinimum(self.min)
        self._slider.setMaximum(self.max)
        self._slider.sliderMoved.connect(self.updateSlider)

        self._main_layout.addWidget(self._slider)
        self._main_layout.addWidget(self._text)

        self.setText(str(def_))
        self._slider.setValue(def_)

    def read_data(self):
        return [max(min(int(self.text()), self.max), self.min)]

    def updateSlider(self, v):
        self.setText(u"%d" % v)

    def setText(self, s):
        self._text.setText(s)

    def text(self):
        return self._text.text()


class FloatSlider(Widget):
    def __init__(self, min=0, max=1, def_=0):
        self.min = float(min)
        self.max = float(max)
        super(FloatSlider, self).__init__()
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)

        self._text = QLineEdit()
        self._text.setFixedWidth(60)

        self._slider = QSlider(Qt.Horizontal, self)
        self._slider.setMinimum(0)
        self._slider.setMaximum(1000000)
        self._slider.sliderMoved.connect(self.updateSlider)

        self._main_layout.addWidget(self._slider)
        self._main_layout.addWidget(self._text)

        self.setText(u"%.3f" % def_)
        self._slider.setValue(def_)

    def read_data(self):
        return [max(min(float(self.text()), self.max), self.min)]

    def updateSlider(self, v):
        size = self.max - self.min
        v = max(min(float(v) / 1000000, 1), 0)
        v = (v * size) + self.min
        v = max(min(v, self.max), self.min)
        self.setText("%.3f" % v)

    def setText(self, s):
        self._text.setText(s)

    def text(self):
        return self._text.text()


class HBoxLayout(Widget):
    def __init__(self, childs, margins=5, spacing=5, align=None):
        super(HBoxLayout, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(margins, margins, margins, margins)
        self.main_layout.setSpacing(spacing)
        if align == 'left':
            self.main_layout.setAlignment(Qt.AlignLeft)
        elif align == 'right':
            self.main_layout.setAlignment(Qt.AlignRight)
        elif align == 'top':
            self.main_layout.setAlignment(Qt.AlignTop)
        elif align == 'bottom':
            self.main_layout.setAlignment(Qt.AlignBottom)
        elif align == 'center':
            self.main_layout.setAlignment(Qt.AlignCenter)

        self.childs = childs
        for i in childs:
            self.main_layout.addWidget(i)

    def read_data(self):
        for i in self.childs:
            data = i.read_data()
            for t in data:
                yield t


class VBoxLayout(Widget):
    def __init__(self, childs, margins=5, spacing=5, align=None):
        super(VBoxLayout, self).__init__()
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(margins, margins, margins, margins)
        self.main_layout.setSpacing(spacing)
        if align == 'left':
            self.main_layout.setAlignment(Qt.AlignLeft)
        elif align == 'right':
            self.main_layout.setAlignment(Qt.AlignRight)
        elif align == 'top':
            self.main_layout.setAlignment(Qt.AlignTop)
        elif align == 'bottom':
            self.main_layout.setAlignment(Qt.AlignBottom)
        elif align == 'center':
            self.main_layout.setAlignment(Qt.AlignCenter)

        self.childs = childs
        for i in childs:
            self.main_layout.addWidget(i)

    def read_data(self):
        for i in self.childs:
            data = i.read_data()
            for t in data:
                yield t


class FormLayout(Widget):
    def __init__(self, childs, margins=5, spacing=5, align=None):
        super(FormLayout, self).__init__()
        self.main_layout = QFormLayout(self)
        self.main_layout.setContentsMargins(margins, margins, margins, margins)
        self.main_layout.setSpacing(spacing)
        if align == 'left':
            self.main_layout.setAlignment(Qt.AlignLeft)
        elif align == 'right':
            self.main_layout.setAlignment(Qt.AlignRight)
        elif align == 'top':
            self.main_layout.setAlignment(Qt.AlignTop)
        elif align == 'bottom':
            self.main_layout.setAlignment(Qt.AlignBottom)
        elif align == 'center':
            self.main_layout.setAlignment(Qt.AlignCenter)

        self.labels = childs[0::2]
        self.childs = childs[1::2]

        for l, w in zip(self.labels, self.childs):
            self.main_layout.addRow(l, w)

    def read_data(self):
        for i in self.childs:
            data = i.read_data()
            for t in data:
                yield t


class ScrollArea(Widget):
    def __init__(self, widget):
        super(ScrollArea, self).__init__()

        self.widget = widget

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.view = QScrollArea()
        self.view.setWidgetResizable(True)
        self.view.setWidget(self.widget)

        self.main_layout.addWidget(self.view)

    def read_data(self):
        return self.widget.read_data()


class SubmitWidget(Widget):
    def __init__(self, form=tuple(),
                 func=lambda *args: 0,
                 doit_text=u"确认表单已填充-执行",
                 margins=5,
                 spacing=5):
        self.func = call_block(func)
        super(SubmitWidget, self).__init__()

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(margins, margins, margins, margins)
        self.main_layout.setSpacing(spacing)

        # self._head = Head(self)
        # self._main_layout.addWidget(self._head)

        self.widgets = list()
        for i in form:
            self.main_layout.addWidget(i)
            self.widgets.append(i)

        self.doit_bn = QPushButton(doit_text)
        self.doit_bn.clicked.connect(call_block(self.doit))
        self.main_layout.addWidget(self.doit_bn)

    def doit_value(self):
        for i in self.widgets:
            data = i.read_data()
            for t in data:
                yield t

    def doit(self, *args):
        self.func(*self.doit_value())
