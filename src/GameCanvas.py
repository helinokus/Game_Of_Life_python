from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtWidgets import QWidget


class GameCanvas(QWidget):
    """
    Widget Qt do renderowania siatki Gry w Życie.

    Attributes:
        game (GameOfLife): Referencja do instancji logiki gry
        cell_size (int): Rozmiar każdej komórki w pikselach
    """
    def __init__(self, game):
        """
        Inicjalizuje widget canvas gry.

        Args:
            game (GameOfLife): Instancja logiki gry do wizualizacji
        """
        super().__init__()
        self.game = game
        self.cell_size = 10
        self.setFixedSize(self.game.width * self.cell_size, self.game.height * self.cell_size)

    def paintEvent(self, event):
        """
        Obsługuje zdarzenia malowania widgetu do renderowania siatki gry.

        Args:
            event (QPaintEvent): Informacje o zdarzeniu malowania
        """
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(25,25,25))

        painter.setPen(QPen(QColor(255,255,255), 1))
        for i in range(self.game.width + 1):
            x = i * self.cell_size
            painter.drawLine(x, 0, x, self.height())
        for i in range(self.game.height + 1):
            y = i * self.cell_size
            painter.drawLine(0, y, self.width(), y)

        painter.setBrush(QBrush(QColor(204, 0, 103)))
        painter.setPen(QPen(QColor(0, 0, 0), 1))

        for y in range(self.game.height):
            for x in range(self.game.width):
                if self.game.grid[y][x] == 1:
                    painter.drawRect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
