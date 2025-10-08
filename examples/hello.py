# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
import sys

sys.path.append("C:/workspace/ASUS_TUF_GAMING_FI6/dev/my_own/python_for_maya/package/cpform/src")
from cpform.widget.core import *
import cpform.docker as docker

ui = SubmitWidget(
    form=[
        ScrollArea(
            VBoxLayout(
                childs=[
                    Label('Input your name:'),
                    LineEdit(placeholder_text='Name'),
                    Label('Input your age:'),
                    IntegerLineEdit(placeholder_text='Age'),
                    Label('Input your email:'),
                    EmailLineEdit(placeholder_text='Email'),
                ],
                align='top'
            )
        )
    ]
)
docker.default_docker(title='Maya Example', form=ui)
