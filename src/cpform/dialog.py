#!/usr/bin/python
# -*-coding:utf-8 -*-
# pylint: disable=duplicate-code
u"""
:创建时间: 2025/9/23 11:10
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:Github: https://github.com/cpcgskill
:QQ: 2921251087
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
:爱发电: https://afdian.net/@Phantom_of_the_Cang

"""
from __future__ import unicode_literals, print_function, division

# pylint: enable=duplicate-code

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

from cpform.widget.all import *
from cpform.docker import *


def get_open_file_name():
    """
    获得文件路径

    :return: AnyStr
    """
    path = QFileDialog.getOpenFileName()
    if len(path) < 2:
        return None
    return path[0]


def get_save_file_name():
    """
    获得保存文件路径

    :return: AnyStr
    """
    path = QFileDialog.getSaveFileName()
    if len(path) < 2:
        return None
    return path[0]


def get_directory_name():
    """
    获得文件夹路径

    :return: AnyStr
    """
    path = QFileDialog.getExistingDirectory()
    if len(path) < 3:
        return None
    return path


# 提示对话框
def show_message(title, message, icon='info'):
    """
    显示一个消息对话框

    :param title: 标题
    :param message: 消息内容
    :param icon: 图标类型， 可选值有 'info', 'warning', 'error', 'question'
    """
    dialog_docker(
        form=VBoxLayout(
            childs=[
                HBoxLayout(
                    childs=[
                        Icon(icon=icon, size='x1.6'),
                        Label(
                            text=message,
                            word_wrap=True,
                        ),
                    ],
                    margins=0,
                ),
                'stretch',
                HBoxLayout(
                    childs=[
                        AttentionButton(
                            text='确定',
                            func=lambda: quit_dialog_docker()
                        ),
                    ],
                    align='right',
                    margins=0,
                )
            ],
            margins='x3',
        ),
        title=title,
    )


# 确认对话框
def show_confirm(title, message, icon='help-circle'):
    """
    显示一个确认对话框

    :param title: 标题
    :param message: 消息内容
    :param icon: 图标类型， 可选值有 'info', 'warning', 'error', 'question'
    :return: bool, 用户点击了确定返回 True, 点击了取消返回 False
    """
    result = {'value': False}

    def on_confirm():
        result['value'] = True
        quit_dialog_docker()

    def on_cancel():
        result['value'] = False
        quit_dialog_docker()

    dialog_docker(
        form=VBoxLayout(
            childs=[
                HBoxLayout(
                    childs=[
                        Icon(icon=icon, size='x1.6'),
                        Label(
                            text=message,
                            word_wrap=True,
                        ),
                    ],
                    margins=0,
                ),
                'stretch',
                HBoxLayout(
                    childs=[
                        NormalButton(
                            text='取消',
                            func=on_cancel
                        ),
                        AttentionButton(
                            text='确定',
                            func=on_confirm
                        ),
                    ],
                    align='right',
                    margins=0,
                )
            ],
            margins='x3',
        ),
        title=title,
    )

    return result['value']

def show_input(title, message, default_text='', placeholder_text='请输入内容'):
    """
    显示一个输入对话框

    :param title: 标题
    :param message: 消息内容
    :param default_text: 默认文本
    :param placeholder_text: 占位符文本
    :return: str or None, 用户点击了确定返回输入的文本, 点击了取消返回 None
    """
    result = {'value': None}

    line_edit = LineEdit(
        text=default_text,
        placeholder_text=placeholder_text,
    )

    def on_confirm():
        result['value'] = line_edit.get_text()
        quit_dialog_docker()

    def on_cancel():
        result['value'] = None
        quit_dialog_docker()

    dialog_docker(
        form=VBoxLayout(
            childs=[
                Label(
                    text=message,
                    word_wrap=True,
                ),
                line_edit,
                'stretch',
                HBoxLayout(
                    childs=[
                        NormalButton(
                            text='取消',
                            func=on_cancel
                        ),
                        AttentionButton(
                            text='确定',
                            func=on_confirm
                        ),
                    ],
                    align='right',
                    margins=0,
                )
            ],
            margins='x3',
        ),
        title=title,
    )

    return result['value']

def show_multi_line_input(title, message, default_text='', placeholder_text='请输入内容'):
    """
    显示一个多行输入对话框

    :param title: 标题
    :param message: 消息内容
    :param default_text: 默认文本
    :param placeholder_text: 占位符文本
    :return: str or None, 用户点击了确定返回输入的文本, 点击了取消返回 None
    """
    result = {'value': None}

    text_edit = TextEditWidget(
        text=default_text,
        placeholder_text=placeholder_text,
    )

    def on_confirm():
        result['value'] = text_edit.get_plain_text()
        quit_dialog_docker()

    def on_cancel():
        result['value'] = None
        quit_dialog_docker()

    dialog_docker(
        form=VBoxLayout(
            childs=[
                Label(
                    text=message,
                    word_wrap=True,
                ),
                text_edit,
                'stretch',
                HBoxLayout(
                    childs=[
                        NormalButton(
                            text='取消',
                            func=on_cancel
                        ),
                        AttentionButton(
                            text='确定',
                            func=on_confirm
                        ),
                    ],
                    align='right',
                    margins=0,
                )
            ],
            margins='x3',
        ),
        title=title,
    )

    return result['value']

def show_multi_input(title, message, fields):
    """
    显示一个多输入对话框

    :param title: 标题
    :param message: 消息内容
    :param fields: 字段列表, 每个字段是一个字典, 包含 'key', 'label', 'default_text', 'placeholder_text' 键
    :return: dict or None, 用户点击了确定返回输入的文本字典, 点击了取消返回 None
    """
    result = {'value': None}
    line_edits = {}

    field_layouts = []
    for field in fields:
        key = field.get('key', field.get('label', ''))
        label = field.get('label', '')
        default_text = field.get('default_text', '')
        placeholder_text = field.get('placeholder_text', '请输入内容')

        line_edit = LineEdit(
            text=default_text,
            placeholder_text=placeholder_text,
        )
        line_edits[key] = line_edit

        field_layouts.append(
            HBoxLayout(
                childs=[
                    Label(text=label, fixed_width=80),
                    line_edit,
                ],
                margins=0,
            )
        )

    def on_confirm():
        result['value'] = {key: le.get_text() for key, le in line_edits.items()}
        quit_dialog_docker()

    def on_cancel():
        result['value'] = None
        quit_dialog_docker()

    dialog_docker(
        form=VBoxLayout(
            childs=[
                Label(
                    text=message,
                    word_wrap=True,
                ),
                VBoxLayout(
                    childs=field_layouts,
                    margins=0,
                ),
                'stretch',
                HBoxLayout(
                    childs=[
                        NormalButton(
                            text='取消',
                            func=on_cancel
                        ),
                        AttentionButton(
                            text='确定',
                            func=on_confirm
                        ),
                    ],
                    align='right',
                    margins=0,
                )
            ],
            margins='x3',
        ),
        title=title,
    )

    return result['value']