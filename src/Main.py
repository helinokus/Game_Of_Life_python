import tkinter as tk

CELL_SIZE = 20
WIDTH = 50
HEIGHT = 50


class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gра в жизнь — Conway")

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas_frame = tk.Frame(main_frame)
        self.canvas_frame.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(
            self.canvas_frame,
            width=WIDTH * CELL_SIZE,
            height=HEIGHT * CELL_SIZE,
            bg="white",
            highlightthickness=2,
            highlightbackground="red"
        )
        self.canvas.pack()

        self.control_frame = tk.Frame(main_frame, padx=10, pady=10, bg="lightgray")
        self.control_frame.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(self.control_frame, text="Управление", bg="lightgray").pack(pady=10)

        tk.Button(self.control_frame, text="Показать квадрат", command=self.draw_test_square).pack(pady=5)
        tk.Button(self.control_frame, text="Показать большой квадрат", command=self.draw_big_square).pack(pady=5)
        tk.Button(self.control_frame, text="Показать сетку", command=self.draw_grid).pack(pady=5)
        tk.Button(self.control_frame, text="Очистить", command=self.clear_canvas).pack(pady=5)

    def draw_test_square(self):
        print("Рисуем квадрат...")
        self.canvas.delete("all")
        # Рисуем квадрат с черной границей и смещением от края
        self.canvas.create_rectangle(
            10, 10, 10 + CELL_SIZE, 10 + CELL_SIZE,
            fill="red",
            outline="black",
            width=2
        )

    def draw_big_square(self):
        print("Рисуем большой квадрат...")
        self.canvas.delete("all")
        # Рисуем большой квадрат в центре
        center_x = (WIDTH * CELL_SIZE) // 2
        center_y = (HEIGHT * CELL_SIZE) // 2
        size = CELL_SIZE * 3

        self.canvas.create_rectangle(
            center_x - size // 2, center_y - size // 2,
            center_x + size // 2, center_y + size // 2,
            fill="blue",
            outline="black",
            width=3
        )

    def draw_grid(self):
        print("Рисуем сетку...")
        self.canvas.delete("all")

        # Рисуем вертикальные линии
        for i in range(WIDTH + 1):
            x = i * CELL_SIZE
            self.canvas.create_line(x, 0, x, HEIGHT * CELL_SIZE, fill="lightgray")

        # Рисуем горизонтальные линии
        for i in range(HEIGHT + 1):
            y = i * CELL_SIZE
            self.canvas.create_line(0, y, WIDTH * CELL_SIZE, y, fill="lightgray")

    def clear_canvas(self):
        print("Очищаем canvas...")
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    app = GameGUI(root)
    root.mainloop()