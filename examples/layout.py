# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
import sys

sys.path.append("C:/workspace/ASUS_TUF_GAMING_FI6/dev/my_own/python_for_maya/package/cpform/src")
from cpform.widget.core import *
import cpform.docker as docker

ui = VBoxLayout(
    childs=[
        SuccessButton(text='button1'),
        WarningButton(text='button2'),
        ErrorButton(text='button3'),
    ],
    align='top'
)
docker.scalable_view_docker(title='VBoxLayout Example', form=ui)

ui = HBoxLayout(
    childs=[
        SuccessButton(text='button1'),
        WarningButton(text='button2'),
        ErrorButton(text='button3'),
    ],
    align='top'
)
docker.scalable_view_docker(title='HBoxLayout Example', form=ui)

ui = FormLayout(
    childs=[
        'Name', LineEdit(placeholder_text='Name'),
        'Age', LineEdit(placeholder_text='Age'),
        'Email', LineEdit(placeholder_text='Email'),
    ]
)
docker.scalable_view_docker(title='FormLayout Example', form=ui)
