class BerryField:
    def __init__(self, berry_field, active_bears, reserve_bears, active_tourists, reserve_tourists):
        self.board = berry_field
        self.active_bears = active_bears
        self.reserve_bears = reserve_bears
        self.active_tourists = active_tourists
        self.reserve_tourists = reserve_tourists


    def get_berries_count(self):
        count = 0
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                count += self.board[r][c]
        return count


    def step(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] >= 1 and self.board[r][c] < 10:
                    self.board[r][c] += 1

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == 0:
                    grow = False
                    if r > 0 and self.board[r - 1][c] == 10:
                        grow = True
                    if r < len(self.board) - 1 and self.board[r + 1][c] == 10:
                        grow = True
                    if c > 0 and self.board[r][c - 1] == 10:
                        grow = True
                    if c < len(self.board) - 1 and self.board[r][c + 1] == 10:
                        grow = True
                    if grow:
                        self.board[r][c] = 1


    def __str__(self):
        s = 'Field has {} berries.\n'.format(self.get_berries_count())

        board = []
        for r in range(len(self.board)):
            rows = []
            for c in range(len(self.board[r])):
                rows.append(self.board[r][c])
            board.append(rows)
        
        for active_tourist in self.active_tourists:
            board[active_tourist.row][active_tourist.col] = 'T'


        for active_bear in self.active_bears:
            if board[active_bear.row][active_bear.col] == 'T':
                board[active_bear.row][active_bear.col] = 'X'
                active_bear.asleep = 3
            else:
                board[active_bear.row][active_bear.col] = 'B'

        for r in range(len(board)):
            for c in range(len(board[r])):
                s += '{:>4}'.format(board[r][c])
            s += '\n'

        s += '\nActive Bears:\n'
        for active_bear in self.active_bears:
            s += str(active_bear) + '\n'

        s += '\nActive Tourists:\n'
        for active_tourist in self.active_tourists:
            s += str(active_tourist) + '\n'
        return s


    def next_turn(self):
        self.update_tourist()
        self.update_berry()
        self.update_bear()
        self.update_tourist2()


    def update_tourist(self):
        tourists = []
        for active_tourist in self.active_tourists:
            left = False
            count = 0
            for active_bear in self.active_bears:
                if active_bear.row == active_tourist.row and active_bear.col == active_tourist.col:
                    left = True
                if active_bear.get_distance(active_tourist.row, active_tourist.col) <= 4:
                    count += 1
            if left or count >= 3:
                tourists.append(active_tourist)
                print('{} - Left the Field'.format(active_tourist))
            if count == 0 and active_tourist.turns == 2:
                tourists.append(active_tourist)
                print('{} - Left the Field'.format(active_tourist))
        for tourist in tourists:
            self.active_tourists.remove(tourist)

    def update_tourist2(self):
        tourists = []
        for active_tourist in self.active_tourists:
            left = False
            count = 0
            for active_bear in self.active_bears:
                if active_bear.row == active_tourist.row and active_bear.col == active_tourist.col:
                    left = True
                if active_bear.get_distance(active_tourist.row, active_tourist.col) <= 4:
                    count += 1
            if left or count >= 3:
                tourists.append(active_tourist)
            if count == 0:
                active_tourist.turns += 1
            else:
                active_tourist.turns = 0
        for tourist in tourists:
            self.active_tourists.remove(tourist)


    def update_berry(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if 1 <= self.board[r][c] < 10:
                    self.board[r][c] += 1
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == 0:
                    grow = False
                    if r > 0 and self.board[r - 1][c] == 10:
                        grow = True
                    if r < len(self.board) - 1 and self.board[r + 1][c] == 10:
                        grow = True
                    if c > 0 and self.board[r][c - 1] == 10:
                        grow = True
                    if c < len(self.board[r]) - 1 and self.board[r][c + 1] == 10:
                        grow = True
                    if r > 0 and c > 0 and self.board[r - 1][c - 1] == 10:
                        grow = True
                    if r > 0 and c < len(self.board[r]) - 1 and self.board[r - 1][c + 1] == 10:
                        grow = True
                    if r < len(self.board) - 1 and c > 0 and self.board[r + 1][c - 1] == 10:
                        grow = True
                    if r < len(self.board) - 1 and c < len(self.board[r]) - 1 and self.board[r + 1][c + 1] == 10:
                        grow = True
                    if grow:
                        self.board[r][c] = 1


    def update_bear(self):
        bears = []
        for bear in self.active_bears:
            if bear.asleep > 0:
                bear.asleep -= 1
                continue
            berries = 30
            while berries > 0:
                eat = min(berries, self.board[bear.row][bear.col])
                berries -= eat
                self.board[bear.row][bear.col] -= eat
                if berries > 0:
                    bear.move()
                if bear.row == -1 or bear.row == len(self.board) or bear.col == -1 or bear.col == len(self.board[0]):
                    bears.append(bear)
                    print(str(bear) + ' - Left the Field')
                    break
                has_tourist = False
                for active_tourist in self.active_tourists:
                    if bear.row == active_tourist.row and bear.col == active_tourist.col:
                        bears.append(bear)
                        has_tourist = True
                        break
                if has_tourist:
                    break
        for bear in bears:
            self.active_bears.remove(bear)

    def part3_turn(self):
        self.active_bear_3()
        self.active_tourist_3()

    def active_bear_3(self):
        if self.reserve_bears and self.get_berries_count() >= 500:
            bear = self.reserve_bears.pop(0)
            bear.is_active = True
            self.active_bears.append(bear)
            print(str(bear) + ' - Entered the Field')
    
    def active_tourist_3(self):
        if self.reserve_tourists and self.active_bears:
            tourist = self.reserve_tourists.pop(0)
            self.active_tourists.append(tourist)
            print(str(tourist) + ' - Entered the Field')
    
    def end(self):
        return (not self.active_bears and not self.reserve_bears) or (not self.active_bears and self.get_berries_count() == 0)