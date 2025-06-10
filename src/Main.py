import sys

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QApplication, QLabel, QSlider

from src.GameCanvas import GameCanvas
from src.GameOfLife import GameOfLife


class ConwayMainWindow(QMainWindow):

    """
    Główne okno aplikacji dla Gry w Życie Conwaya.

    Zapewnia interfejs użytkownika z wizualizacją gry i przyciskami sterowania.

    Attributes:
        game (GameOfLife): Instancja logiki gry
        canvas (GameCanvas): Widget wizualny do wyświetlania gry
        is_running (bool): Aktualny stan symulacji
        timer (QTimer): Timer do automatycznych kroków symulacji
        speed_slider (QSlider): Kontrolka prędkości symulacji
        speed_value_label (QLabel): Wyświetlanie aktualnego ustawienia prędkości
    """

    def __init__(self):
        """
        Inicjalizuje główne okno aplikacji.
        """
        super().__init__()
        self.setWindowTitle("Conway's Game of Life")

        self.game = GameOfLife(50, 50, 5)
        self.canvas = GameCanvas(self.game)
        self.is_running = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.step)

        self.setup_ui()

    def setup_ui(self):
        """
        Tworzy i układa elementy interfejsu użytkownika.
        """
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(25)

        self.canvas = GameCanvas(self.game)
        main_layout.addWidget(self.canvas, 75)

        control_layout = QVBoxLayout()

        btn_random = QPushButton("Wygeneruj randomowo")
        btn_random.clicked.connect(self.generate_random)
        control_layout.addWidget(btn_random)

        btn_clear = QPushButton("Wyczysc")
        btn_clear.clicked.connect(self.clear_grid)
        control_layout.addWidget(btn_clear)

        btn_start = QPushButton("Start")
        btn_start.clicked.connect(self.start_simulation)
        control_layout.addWidget(btn_start)

        btn_stop = QPushButton("Stop")
        btn_stop.clicked.connect(self.stop_simulation)
        control_layout.addWidget(btn_stop)

        btn_step = QPushButton("Krok")
        btn_step.clicked.connect(self.step)
        control_layout.addWidget(btn_step)

        speed_label = QLabel("Predkość:")
        control_layout.addWidget(speed_label)

        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 200)
        self.speed_slider.setValue(25)
        self.speed_slider.valueChanged.connect(self.update_simulation_speed)
        control_layout.addWidget(self.speed_slider)

        self.speed_value_label = QLabel(f"Prędkość teraz: {self.speed_slider.value()} ms")
        control_layout.addWidget(self.speed_value_label)

        control_layout.addStretch()

        main_layout.addLayout(control_layout)

        self.setFixedSize(self.canvas.width() + 250, self.canvas.height()+100)

    def generate_random(self):
        """Generuje nową losową konfigurację początkową."""
        self.game.clear()
        self.game.init_grid(5)
        self.canvas.update()

    def clear_grid(self):
        """Czyści całą siatkę gry."""
        self.game.clear()
        self.canvas.update()

    def start_simulation(self):
        """Rozpoczyna automatyczną symulację jeśli nie jest już uruchomiona."""
        if not self.is_running:
            self.is_running = True
            self.timer.start(self.speed_slider.value())

    def stop_simulation(self):
        """Zatrzymuje automatyczną symulację jeśli jest obecnie uruchomiona."""
        if self.is_running:
            self.is_running = False
            self.timer.stop()

    def step(self):
        """Wykonuje pojedynczy krok symulacji."""
        self.game.update()
        self.canvas.update()

    def update_simulation_speed(self):
        """Aktualizuje prędkość symulacji na podstawie wartości slidera."""
        new_speed = self.speed_slider.value()
        self.timer.setInterval(new_speed)
        self.speed_value_label.setText(f"Prędkość teraz: {new_speed} ms")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConwayMainWindow()
    window.show()
    sys.exit(app.exec_())