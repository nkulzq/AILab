import time


class Board:
    def __init__(self, canvas, size=4):
        self.canvas = canvas
        self.size = size
        self.square_size = 400 // size
        canvas_width = self.square_size * size
        canvas_height = self.square_size * size
        canvas.config(width=canvas_width, height=canvas_height)
        self.piece_radius = self.square_size // 4
        self.res = [-1] * self.size
        self.num_solutions = 0
        self.draw_board()
        self.solver = self.solve(0)
        self.finish = False

    def reset(self):
        self.square_size = 400 // self.size
        canvas_width = self.square_size * self.size
        canvas_height = self.square_size * self.size
        self.canvas.config(width=canvas_width, height=canvas_height)
        self.piece_radius = self.square_size // 4
        self.res = [-1] * self.size
        self.num_solutions = 0
        self.draw_board()
        self.solver = self.solve(0)
        self.finish = False

    def clear_board(self):
        self.canvas.delete('pieces')

    def draw_board(self):
        square_size = 400 // self.size
        for row in range(self.size):
            for col in range(self.size):
                x1 = col * square_size
                y1 = row * square_size
                x2 = x1 + square_size
                y2 = y1 + square_size
                color = 'black' if (row + col) % 2 == 0 else 'white'
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')

    def draw_solution(self):
        for row, col in enumerate(self.res):
            if col != -1:
                x_center = col * self.square_size + self.square_size // 2
                y_center = row * self.square_size + self.square_size // 2
                self.canvas.create_oval(
                    x_center - self.piece_radius,
                    y_center - self.piece_radius,
                    x_center + self.piece_radius,
                    y_center + self.piece_radius,
                    fill='red', tags='pieces')

    def check(self, col, row):
        for i in range(row):
            if self.res[i] == col or self.res[i] + i == row + col or self.res[i] - i == col - row:
                return False
        return True

    def solve(self, row):
        self.clear_board()
        self.draw_solution()
        yield
        if row == self.size:
            self.num_solutions += 1
            return
        for col in range(self.size):
            if self.check(col, row):
                self.res[row] = col
                yield from self.solve(row + 1)
                self.res[row] = -1
                self.clear_board()
                self.draw_solution()
                yield

    def solve_continuous(self):
        while True:
            try:
                next(self.solver)
                self.canvas.update()
            except StopIteration:
                self.finish = True
                break

    def solve_step(self):
        try:
            next(self.solver)
        except StopIteration:
            self.finish = True



