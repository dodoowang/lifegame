import random
import fire


class Grid():

    def __init__(self, size=10, pattern=""):
        # generate a grid with size (default is 10 * 10)
        # internal data size will be (size + 2) * (size + 2), to avoid
        # out of range operation
        # if size == 0, then keep the current states
        if size == 0:
            pass
        else:
            self.size = size
            self.data = [[0 for i in range(size + 2)] for j in range(size + 2)]
        if pattern == "":
            pass
        else:
            self.create_the_world(pattern)

    def create_the_world(self, pattern):
        # create the world with pattern of cells specified
        # if pattern is a number, then randomly generate this number of cells
        # on the grid
        # if pattern is a string of comma separated binary numbers like
        # "10001, 11100, 11110, 00001", each 1 is a living cell to be created
        # if pattern is a file, load the predefined pattern from the file
        if isinstance(pattern, int):
            num = pattern
            cells = random.sample(range(self.size*self.size), num)
            for pos in cells:
                self.data[pos // self.size + 1][pos % self.size + 1] = 1
        if isinstance(pattern, str):
            pattern = pattern.strip()
            if ',' in pattern:
                pos_xy = self.size // 2
                pattern = map(str.strip, pattern.split(','))
                pattern = [list(map(int, list(x))) for x in pattern]
                print(pattern)
                for idx, row in enumerate(pattern):
                    self.data[pos_xy + idx][pos_xy: pos_xy + len(row)] = row
            if '.' in pattern:
                pos_xy = self.size // 2
                pattern = [list(map(int, list(x.strip()))) for x in
                           open(pattern).readlines()]
                print(pattern)
                for idx, row in enumerate(pattern):
                    self.data[pos_xy + idx][pos_xy: pos_xy + len(row)] = row

        return self

    def update(self):
        # update the status of every cells on the grid
        size = self.size
        data_next = [[0 for i in range(size + 2)] for j in range(size + 2)]
        for i in range(1, size + 1):
            for j in range(1, size + 1):
                result = self._live_or_die_(i, j)
                if result == 0:
                    data_next[i][j] = 0
                if result == 1:
                    data_next[i][j] = self.data[i][j]
                if result == 2:
                    data_next[i][j] = 1
        self.data = data_next

        return self

    def _live_or_die_(self, i, j):
        # decide next step status based on predefined rules:
        # 0: die.       If the number of live cells nearby <2 or >3
        # 1: live.      If the number of live cells nearby =2
        # 2: reproduce. If the number of live cells nearby =3
        n = sum(self.data[i-1][j-1:j+2])
        n += sum(self.data[i][j-1:j+2])
        n += sum(self.data[i+1][j-1:j+2])
        n -= self.data[i][j]
        if n == 2:
            return 1
        if n == 3:
            return 2
        return 0

    def count(self):
        # return the number of live cells on the grid
        n = sum([sum(x) for x in self.data])
        return n

    def show(self):
        # show the grid on screen
        print("-" * 30 + "cells alive: " + str(self.count()) + "-" * 30)
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                print('.' if self.data[i][j] == 0 else 'o', sep='', end='\t')
            print('\n')

        return self


if __name__ == "__main__":
    fire.Fire(Grid)
