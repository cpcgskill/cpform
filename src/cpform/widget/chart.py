# -*-coding:utf-8 -*-
# pylint: disable=duplicate-code
"""
:创建时间: 2025/9/22 15:40
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
from cpform.config import config_manager
from cpform.widget.core import FormInterface, Background


# 贝塞尔曲线 图表

def _cubic_bezier(pts, u):
    """
    n 阶贝塞尔曲线计算
    :param pts: 控制点列表
    :param u: 参数， 0.0 ~ 1.0
    :return: 点坐标
    """
    if len(pts) == 1:
        return pts[0]
    return _cubic_bezier(
        [
            (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)
            for a, b in zip(pts[:-1], pts[1:])
        ],
        u
    )


class _BezierChart(QWidget):
    def __init__(self, points=None, point_radius=None, lines=None):
        """
        贝塞尔曲线图表
        :param points: 控制点列表， [{'x': 0.0, 'y': 0.0, 'can_move': True, 'show': True}, ...]
        x 和 y 的值范围是 0.0 ~ 1.0，表示在图表中的位置比例
        其中 can_move 表示该点是否可以被用户拖动
        其中 show 表示该点是否显示, 默认跟随 can_move 一起变化。但是可以单独设置。
        :param point_radius: 控制点的半径， 默认 config_manager.LineWidthThick * 2
        :param lines: 预留参数，暂未使用
        线段列表， [{'start': 0, 'end': 1}, ...]
        start 和 end 是 points 列表中的索引，表示该线段连接的两个点
        线段会以虚线形式绘制在图表上，辅助参考
        该参数可以为空，表示不绘制线段
        :return:
        """
        super(_BezierChart, self).__init__()
        # 全局监听鼠标
        self.setMouseTracking(True)
        #
        self.setMinimumSize(QSize(20, 20))
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        #
        self.points = points if points is not None else []
        self.selected_point_index = -1  # 当前选中的点索引
        self.over_point_index = -1  # 当前悬停的点索引
        if point_radius is None:
            self.point_radius = config_manager.LineWidthThick * 2
        else:
            self.point_radius = point_radius
        self.lines = lines if lines is not None else []

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            w = self.width() - config_manager.LineWidth * 8
            h = self.height() - config_manager.LineWidth * 8
            x = event.pos().x() - config_manager.LineWidth * 4
            y = event.pos().y() - config_manager.LineWidth * 4
            for i, p in enumerate(self.points):
                if not p.get('can_move', True):
                    continue
                px = p['x'] * w
                py = p['y'] * h
                dist_sq = (px - x) ** 2 + (py - y) ** 2
                if dist_sq <= self.point_radius ** 3:
                    self.selected_point_index = i
                    self.update()
                    break
        super(_BezierChart, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.selected_point_index != -1:
            w = self.width() - config_manager.LineWidth * 8
            h = self.height() - config_manager.LineWidth * 8
            x = event.pos().x() - config_manager.LineWidth * 4
            y = event.pos().y() - config_manager.LineWidth * 4
            # 限制在范围内
            x = max(0, min(w, x))
            y = max(0, min(h, y))
            p = self.points[self.selected_point_index]
            p['x'] = x / w
            p['y'] = y / h
            self.update()
        else:
            w = self.width() - config_manager.LineWidth * 8
            h = self.height() - config_manager.LineWidth * 8
            x = event.pos().x() - config_manager.LineWidth * 4
            y = event.pos().y() - config_manager.LineWidth * 4
            over_index = -1
            for i, p in enumerate(self.points):
                if not p.get('can_move', True):
                    continue
                px = p['x'] * w
                py = p['y'] * h
                dist_sq = (px - x) ** 2 + (py - y) ** 2
                if dist_sq <= self.point_radius ** 3:
                    over_index = i
                    break
            if over_index != self.over_point_index:
                self.over_point_index = over_index
                if self.over_point_index != -1:
                    self.setCursor(Qt.CursorShape.PointingHandCursor)
                else:
                    self.setCursor(Qt.CursorShape.ArrowCursor)
                self.update()
        super(_BezierChart, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.selected_point_index = -1
            self.update()
        super(_BezierChart, self).mouseReleaseEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        w = self.width() - config_manager.LineWidth * 8
        h = self.height() - config_manager.LineWidth * 8
        painter.translate(config_manager.LineWidth * 4, config_manager.LineWidth * 4)
        # 背景网格
        grid_size = 0.1
        # 线段 线
        painter.setPen(QPen(QColor(config_manager.LineColorWeak), config_manager.LineWidthThin, Qt.PenStyle.SolidLine))
        for x in range(int(1 / grid_size) + 1):
            gx = x * grid_size * w
            painter.drawLine(gx, 0, gx, h)
        for y in range(int(1 / grid_size) + 1):
            gy = y * grid_size * h
            painter.drawLine(0, gy, w, gy)

        # 绘制曲线, 调用Qt自带的贝塞尔曲线绘制
        if len(self.points) >= 2:
            draw_points = [QPointF(p['x'] * w, p['y'] * h) for p in self.points]
            painter.setPen(
                QPen(QColor(config_manager.LineColorAttention), config_manager.LineWidthThick, Qt.PenStyle.SolidLine))
            painter.setBrush(Qt.BrushStyle.NoBrush)
            path = QPainterPath()
            path.moveTo(draw_points[0])
            for i in range(1, len(draw_points), 3):
                if i + 2 < len(draw_points):
                    path.cubicTo(draw_points[i], draw_points[i + 1], draw_points[i + 2])
                elif i + 1 < len(draw_points):
                    path.quadTo(draw_points[i], draw_points[i + 1])
                else:
                    path.lineTo(draw_points[i])
            painter.drawPath(path)

        # 绘制连接控制点的线
        if len(self.points) >= 2 and self.lines:
            painter.setPen(QPen(QColor(config_manager.LineColor), config_manager.LineWidth, Qt.PenStyle.DotLine))
            for line in self.lines:
                start_index = line.get('start', 0)
                end_index = line.get('end', 1)
                if start_index < 0 or start_index >= len(self.points):
                    continue
                if end_index < 0 or end_index >= len(self.points):
                    continue
                p1 = self.points[start_index]
                p2 = self.points[end_index]
                painter.drawLine(
                    p1['x'] * w, p1['y'] * h,
                    p2['x'] * w, p2['y'] * h,
                )

        # 绘制控制点
        for i, p in enumerate(self.points):
            if not p.get('show', p.get('can_move', True)):
                continue
            px = p['x'] * w
            py = p['y'] * h
            rect = QRectF(
                px - self.point_radius,
                py - self.point_radius,
                self.point_radius * 2,
                self.point_radius * 2
            )
            painter.setPen(QPen(QColor(config_manager.PrimaryColor), config_manager.LineWidthThick))
            if i == self.over_point_index:
                painter.setBrush(QBrush(QColor(config_manager.LineColorAttention)))
            else:
                painter.setBrush(QBrush(QColor(config_manager.LineColor)))
            painter.drawEllipse(rect)

        painter.end()


def bezier_chart(points=None, point_radius=None, lines=None):
    """
    创建贝塞尔曲线图表
    :param points: 控制点列表， [{'x': 0.0, 'y': 0.0, 'can_move': True, 'show': True}, ...]
    x 和 y 的值范围是 0.0 ~ 1.0，表示在图表中的位置比例
    其中 can_move 表示该点是否可以被用户拖动
    其中 show 表示该点是否显示, 默认跟随 can_move 一起变化。但是可以单独设置。
    :return:
    """
    chart = _BezierChart(points=points, point_radius=point_radius, lines=lines)
    return Background(
        child=chart,
    )


# todo: nurbs

# todo: 拉格朗日曲线

# todo: 折线图

# todo: 柱状图

# todo: 饼图

# todo: 雷达图

# todo: 散点图

# todo: 热力图

# todo: DG 图

# todo: 关系图


if __name__ == '__main__':
    from cpform.docker import default_docker
    from cpform.widget.core import VBoxLayout, HBoxLayout

    default_docker(
        form=VBoxLayout(
            childs=[
                bezier_chart(
                    points=[
                        {'x': 0.0, 'y': 0.0, 'can_move': False, 'show': True},
                        {'x': 0.5, 'y': 0.0, 'can_move': True},
                        {'x': 0.5, 'y': 1.0, 'can_move': True},
                        {'x': 1.0, 'y': 1.0, 'can_move': False, 'show': True},
                    ],
                    lines=[
                        {'start': 0, 'end': 1},
                        {'start': 2, 'end': 3},
                    ]
                ),
                nurbs_chart(
                    points=[
                        {'x': 0.0, 'y': 0.0, 'can_move': False, 'show': True},
                        {'x': 0.3, 'y': 0.8, 'can_move': True},
                        {'x': 0.6, 'y': 0.2, 'can_move': True},
                        {'x': 1.0, 'y': 1.0, 'can_move': False, 'show': True},
                    ],
                    lines=[
                        {'start': 0, 'end': 1},
                        {'start': 1, 'end': 2},
                        {'start': 2, 'end': 3},
                    ]
                ),
            ],
        )
    )
    app.exec_()
