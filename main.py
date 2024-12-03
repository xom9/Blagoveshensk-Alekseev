from math import cos, pi, sin
import random
import sys
from PyQt6.QtCore import Qt, QPoint, QPointF
from PyQt6.QtGui import QKeyEvent, QMouseEvent, QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.figure = None
        self.coor = None

        self.init_ui()
        self.setMouseTracking(True)

    def init_ui(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.qp = QPainter()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.figure = 'circle'
            self.drawf()
        elif event.button() == Qt.MouseButton.RightButton:
            self.figure = 'square'
            self.drawf()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.coor = event.pos()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Space:
            self.figure = 'triangle'
            self.drawf()

    def drawf(self):
        self.flag = True
        self.update()

    def draw_figure(self):
        if self.figure == 'circle':
            r = random.randint(20, 100)
            self.qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.qp.drawEllipse(QPointF(self.coor.x(), self.coor.y()), r, r)
        elif self.figure == 'square':
            a = random.randint(20, 100)
            self.qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.qp.drawRect(int(self.coor.x() - a / 2), int(self.coor.y() - a / 2), a, a)
        elif self.figure == 'triangle':
            a = random.randint(20, 100)
            self.qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            x, y = self.coor.x(), self.coor.y()

            points = [
                QPoint(x, y - a),
                QPoint(int(x + cos(7 * pi / 6) * a),
                       int(y - sin(7 * pi / 6) * a)),
                QPoint(int(x + cos(11 * pi / 6) * a),
                       int(y - sin(11 * pi / 6) * a))
            ]

            self.qp.drawPolygon(points)

    def paintEvent(self, event) -> None:
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_figure()
            self.qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Suprematism()
    win.show()
    sys.exit(app.exec())