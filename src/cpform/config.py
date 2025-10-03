# -*-coding:utf-8 -*-
# pylint: disable=duplicate-code
u"""
:创建时间: 2022/4/22 3:50
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
import os

DEBUG = True


class Config(object):
    # 路径 & 字体
    DefaultIcon = os.sep.join([os.path.dirname(os.path.abspath(__file__)), 'assets', 'icon.png'])
    Font = "OPPO Sans Medium"
    FontSize = 14

    # 背景颜色
    BackgroundColor = '#444444'

    # 颜色 (前景/主/注意/成功/警告/错误)
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

    # 覆盖颜色变化
    LightOverlayColorChange = 0.2
    DarkOverlayColorChange = 0.2

    # 圆角等级
    RoundCornersLevel3 = 2  # 最小
    RoundCornersLevel2 = 4  # 中等
    RoundCornersLevel1 = 8  # 最大

    # 线条宽度
    LineWidthThin = 1
    LineWidth = 2
    LineWidthThick = 3

    # 线条颜色
    LineColorWeak = '#484848'
    LineColor = '#505050'
    LineColorAttention = '#666666'

    # 尺寸 & 间距
    Height = 20
    Margin = 2
    Padding = 4
    Spacing = 2

    def as_dict(self):
        """以字典形式返回所有配置项."""
        return {k: v for k, v in self.__class__.__dict__.items() if not k.startswith('_') and not callable(v)}

    def from_dict(self, config_dict):
        """从字典中更新配置项."""
        for k, v in config_dict.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def __init__(self, **kwargs):
        self.from_dict(kwargs)

    def __repr__(self):
        return "UIConfig({})".format(str(self.as_dict())[1:-1])

    def __str__(self):
        return self.__repr__()

    def copy(self):
        """返回当前配置的副本."""
        new_config = Config()
        new_config.from_dict(self.as_dict())
        return new_config


class ConfigManager:
    cf = Config()  # 全局默认配置实例

    def __getattr__(self, item):
        return getattr(ConfigManager.cf, item)

    def __setattr__(self, key, value):
        setattr(ConfigManager.cf, key, value)


config_manager = ConfigManager()  # 全局配置管理器实例
