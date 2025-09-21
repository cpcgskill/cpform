#!/usr/bin/python
# -*-coding:utf-8 -*-
# pylint: disable=duplicate-code
"""
:创建时间: 2025/9/2 18:47
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
import sys

app = QApplication(sys.argv)

try:
    import maya.standalone

    maya.standalone.initialize(name='python')
except:
    pass

from cpform.widget.core import *
import cpform.docker as docker


def base_components():
    return [
        Label('Label'),
        PrimaryButton(text='PrimaryButton', icon='star', func=lambda *args: print('PrimaryButton')),
        AttentionButton(text='AttentionButton', icon='star', func=lambda *args: print('AttentionButton')),
        SuccessButton(text='SuccessButton', icon='check', func=lambda *args: print('SuccessButton')),
        WarningButton(text='WarningButton', icon='alert-circle', func=lambda *args: print('WarningButton')),
        ErrorButton(text='ErrorButton', icon='coffee', func=lambda *args: print('ErrorButton')),
        NormalButton(text='NormalButton', icon='info', func=lambda *args: print('NormalButton')),
        LineEdit('LineEdit1'),
        LineEdit('LineEdit2', True),
        IntegerLineEdit(placeholder_text='Integer LineEdit'),
        FloatLineEdit(placeholder_text='Float LineEdit'),
        EmailLineEdit(placeholder_text='Email LineEdit'),
        IntSlider(2, 10, 3),
        FloatSlider(2, 10, 5),
        CheckBox('CheckBox1', update_func=lambda *args: print('CheckBox1 {}'.format(args))),
        CheckBox('CheckBox2', True, update_func=lambda *args: print('CheckBox2 {}'.format(args))),
        H1('H1'),
        H2('H2'),
        H3('H3'),
        H4('H4'),
        H5('H5'),
        H6('H6'),
    ]


def show():
    ui = ScrollArea(VBoxLayout(
        childs=base_components() + [
            Collapse(
                VBoxLayout(childs=base_components()),
                text='Collapse',
                default_state=True
            ),
            Background(
                VBoxLayout(childs=base_components()),
                '#b0333d'
            ),
        ],
        align='top'
    ))
    docker.scalable_view_docker(title='Test', form=ui)


show()
if sys.version_info.major == 2:
    exec('app.exec_()')
else:
    exec('app.exec_()')
