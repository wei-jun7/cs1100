class Bear:
    def __init__(self, row, col, direction, is_active):
        self.row = row
        self.col = col
        self.direction = direction
        self.is_active = is_active
        self.asleep = 0
    
    def __str__(self):
        s = 'Bear at ({},{}) moving {}'.format(self.row, self.col, self.direction)
        if 0 < self.asleep < 3:
            s += ' - Asleep for {} more turns'.format(self.asleep)
        return s

    def move(self):
        for d in self.direction:
            if d == 'N':
                self.row -= 1
            if d == 'S':
                self.row += 1
            if d == 'E':
                self.col += 1
            if d == 'W':
                self.col -= 1

    def get_distance(self, r, c):
        return abs(self.row - r) + abs(self.col - c)