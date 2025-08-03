# -*-coding:utf-8 -*-
"""
:创建时间: 2024/10/23 18:53
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

绘制器模块， 用于绘制各种元素， 如贝塞尔曲线， 文本， 图片等

"""
from __future__ import unicode_literals, print_function, division

if False:
    from typing import *

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
try:
    from shiboken6 import *
except ImportError:
    try:
        from shiboken2 import *
    except ImportError:
        from shiboken import *

import cpform.config as cf_config


def draw_bezier_curve(painter, points, color=QColor(255, 0, 0), width=2):
    # type: (QPainter, List[QPointF], QColor, int) -> None
    """
    绘制贝塞尔曲线
    :param painter: 画笔
    :param points: 控制点
    :param color: 颜色
    :param width: 线宽
    :return:
    """
    painter.setPen(QPen(color, width))
    painter.setBrush(Qt.BrushStyle.NoBrush)
    path = QPainterPath()
    path.moveTo(points[0])
    for i in range(1, len(points), 3):
        path.cubicTo(points[i], points[i + 1], points[i + 2])
    painter.drawPath(path)


def draw_text(painter, text, rect, color=QColor(cf_config.NormalTextColor), alignment=Qt.AlignmentFlag.AlignCenter):
    # type: (QPainter, str, QRect, QColor, Qt.AlignmentFlag) -> None
    """
    绘制文本
    :param painter: 画笔
    :param text: 文本
    :param rect: 区域
    :param color: 颜色
    :param alignment: 对齐方式
    :return:
    """
    painter.setPen(QPen(color))
    font = QFont(cf_config.Font, cf_config.FontSize)
    painter.setFont(font)
    painter.drawText(rect, alignment, text)

def draw_capsule(painter, rect, line_color=QColor(cf_config.PrimaryColor), fill_color=QColor(cf_config.NormalColor), width=2):
    # type: (QPainter, QRect, QColor, QColor, int) -> None
    """
    绘制胶囊体
    :param painter: 画笔
    :param rect: 区域
    :param line_color: 线颜色
    :param fill_color: 填充颜色
    :param width: 线宽
    :return:
    """
    painter.setPen(QPen(line_color, width))
    painter.setBrush(QBrush(fill_color))
    painter.drawRoundedRect(rect, rect.height() / 2, rect.height() / 2)

if __name__ == '__main__':
    import sys
    import time
    import math


    class TestWidget(QWidget):
        def paintEvent(self, event):
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)

            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QBrush(QColor(*[(math.sin(time.time()) * 0.2 + 0.4) * 255] * 3)))
            painter.drawRect(self.rect())

            draw_bezier_curve(
                painter,
                [
                    QPointF(100, 100), QPointF(200, 200), QPointF(300, 100), QPointF(400, 200),
                    QPointF(500, 100), QPointF(600, 200), QPointF(700, 100)
                ],
                QColor('#cb6200'),
                2
            )

            draw_cf_s = [
                ('AlignCenter', Qt.AlignmentFlag.AlignCenter),
                ('AlignLeftTop', Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop),
                ('AlignLeftCenter', Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter),
                ('AlignLeftBottom', Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom),
                ('AlignRightTop', Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop),
                ('AlignRightCenter', Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter),
                ('AlignRightBottom', Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom),
            ]
            for idx, (text, align) in enumerate(draw_cf_s):
                t_rect = QRect(100, idx * 100 + 200, 200, 100)
                painter.setPen(QPen(QColor(255, 255, 255)))
                painter.setBrush(Qt.BrushStyle.NoBrush)
                painter.drawRect(t_rect)
                draw_text(
                    painter,
                    text,
                    t_rect,
                    QColor(255, 255, 255),
                    align
                )

            draw_capsule(
                painter,
                QRect(300, 200, 200, 100),
                QColor(255, 255, 255),
                QColor(255, 0, 0),
                2
            )

            painter.end()

            self.update()


    app = QApplication(sys.argv)

    w = TestWidget()
    w.resize(800, 600)
    w.show()

    sys.exit(app.exec_())
