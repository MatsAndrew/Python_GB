# task_1
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for row in self.matrix:
            result += f'{" ".join([str(el) for el in row])}\n'
        return result

    def __iadd__(self, other):
        for i in range(len(self.matrix)):
            for el in range(len(self.matrix[i])):
                self.matrix[i][el] += other.matrix[i][el]
        return Matrix.__str__(self)


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_m = Matrix([[6, 5, 4], [3, 2, 1], [0, 0, 0]])
print(m.__iadd__(new_m))
