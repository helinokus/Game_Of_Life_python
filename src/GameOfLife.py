import numpy as np

class GameOfLife:
    """
    Główna implementacja automatu komórkowego "Gra w życie" Conwaya.

    Zarządza stanem gry, stosuje zasady ewolucji i udostępnia metody
    do inicjalizacji i manipulacji siatką komórek.

    Attributes:
        width (int): Szerokość siatki w komórkach
        height (int): Wysokość siatki w komórkach
        grid (numpy.ndarray): Tablica 2D reprezentująca stan komórek (0=martwa, 1=żywa)
    """

    def __init__(self, width, height, density):
        """
        Inicjalizuje nową instancję Gry w Życie.

        Args:
            width (int): Liczba komórek w poziomie
            height (int): Liczba komórek w pionie
            density (int): Parametr gęstości początkowej populacji
        """

        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.init_grid(density)

    def count_neighbors(self, x, y, grid):
        """
        Liczy liczbę żywych sąsiadów dla komórki na pozycji (x, y).

        Args:
            x (int): Współrzędna x komórki
            y (int): Współrzędna y komórki
            grid (numpy.ndarray): Stan siatki do sprawdzenia

        Returns:
            int: Liczba żywych sąsiadów (0-8)
        """

        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if x + dx < 0 or x + dx >= self.width:
                    continue
                if y + dy < 0 or y + dy >= self.height:
                    continue
                nx = x + dx
                ny = y + dy
                count += grid[ny][nx]
                # print(count)
        return count


    def change_cell(self, x, y, grid):
        """
        Stosuje zasady Gry w Życie Conwaya do aktualizacji pojedynczej komórki.

        Args:
            x (int): Współrzędna x komórki
            y (int): Współrzędna y komórki
            grid (numpy.ndarray): Aktualny stan siatki
        """
        neighbors = self.count_neighbors(x, y, grid)
        if grid[y][x] == 0 and neighbors == 3:
            self.grid[y][x] = 1
        elif grid[y][x] == 1 and neighbors in [2, 3]:
            self.grid[y][x] = 1
        else:
            self.grid[y][x] = 0


    def update(self):
        """
        Przeprowadza symulację o jedną generację.

        Tworzy zmianę aktualnego stanu i stosuje zasady ewolucji
        do wszystkich komórek jednocześnie.
        """
        current_state = np.copy(self.grid)

        for y in range(self.height):
            for x in range(self.width):
                self.change_cell(x, y, current_state)

    def init_grid(self, density):
        """
        Inicjalizuje siatkę z losowymi żywymi komórkami.

        Args:
            density (int): Kontrola gęstości populacji. Wyższe wartości tworzą
                         rzadsze początkowe populacje.
        """
        for y in range(self.height):
            for x in range(self.width):
                num = np.random.randint(0, density)
                if num == 0:
                    self.grid[y][x] = 1

    def clear(self):
        """
        Czyści całą siatkę, ustawiając wszystkie komórki jako martwe.
        """
        self.grid = np.zeros((self.height, self.width), dtype=int)

