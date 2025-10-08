# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
import sys

sys.path.append("C:/workspace/ASUS_TUF_GAMING_FI6/dev/my_own/python_for_maya/package/cpform/src")

from cpform.config import config_manager
from cpform.widget.core import *
import cpform.docker as docker

config_manager.PrimaryColor = '#9b59b6'
config_manager.AttentionColor = '#3498db'
config_manager.SuccessColor = '#2ecc71'
config_manager.WarningColor = '#e67e22'
config_manager.ErrorColor = '#e74c3c'
config_manager.NormalColor = '#34495e'
config_manager.BackgroundColor = '#2c3e50'

ui = VBoxLayout(
    childs=[
        SuccessButton(text='button1'),
        WarningButton(text='button2'),
        ErrorButton(text='button3'),
        Label('Input:'),
        LineEdit(placeholder_text='LineEdit'),
    ],
    align='top'
)
docker.scalable_view_docker(title='Style Example', form=ui, size=(800, 600))
