# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/4/22 3:50
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function, division
import os

DEBUG = True

#
DefaultIcon = os.sep.join([os.path.dirname(os.path.abspath(__file__)), 'assets', "icon.png"])

# default font
# Font = "Noto Sans S Chinese Black"
# Font = "zcool-gdh"
# Font = "仓耳渔阳体 W03"
# Font = "微软雅黑"
# Font = "Kingsoft_Cloud_Font"
Font = "OPPO Sans Medium"
FontSize = 14

# 背景颜色
BackgroundColor = '#1A1B1D'

# 颜色
NormalColor = '#5D5D5D'
NormalTextColor = '#FFFFFF'
PrimaryColor = '#38B6BA'
PrimaryTextColor = '#FFFFFF'
AttentionColor = '#31A8FF'
AttentionTextColor = '#FFFFFF'
SuccessColor = '#1abc68'
SuccessTextColor = '#FFFFFF'
WarningColor = '#f1c40f'
WarningTextColor = '#FFFFFF'
ErrorColor = '#e74c3c'
ErrorTextColor = '#FFFFFF'

LightOverlayColorChange = 0.2  # 光线覆盖颜色变化
DarkOverlayColorChange = 0.2  # 暗覆盖颜色变化

RoundCornersLevel3 = 2  # 最小圆角
RoundCornersLevel2 = 4  # 中等圆角
RoundCornersLevel1 = 8  # 最大圆角

LineWidth = 1  # 线条宽度
LineColor = '#505050'  # 线条颜色

Height = 20  # 标准高度
Padding = 4  # 标准内边距
