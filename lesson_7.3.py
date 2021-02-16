# task_3
class Cell:
    def __init__(self, cells_number):
        self.cells_number = cells_number

    def __add__(self, other):
        return Cell(self.cells_number + other.cells_number)

    def __sub__(self, other):
        if self.cells_number - other.cells_number <= 0:
            raise Exception
        return Cell(self.cells_number - other.cells_number)

    def __mul__(self, other):
        return Cell(self.cells_number * other.cells_number)

    def __truediv__(self, other):
        return Cell(self.cells_number // other.cells_number)

    def make_order(self, row):
        pass
