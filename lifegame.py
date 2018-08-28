import random


class Grid():

    def __init__(self, size=10):
        # generate a grid with size (default is 10 * 10)
        # internal data size will be (size + 2) * (size + 2), to pad zero on the edge
        self.size = size
        self.data = [[0 for i in range(size + 2)] for j in range(size + 2)]

    def create_the_world(self, num=20):
        # random create cells on the grid (default 20 cells)
        cells = random.sample(range(self.size*self.size), num)
        for pos in cells:
            self.data[pos // self.size + 1][pos % self.size + 1] = 1

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
        print("-" * 39 + str(self.count()) + "-" * 39)
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                print('.' if self.data[i][j]==0 else 'o', sep='', end='\t')
            print('\n')

    def _show_verbose_(self):
        # show the grid on screen
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                print('.' + str(self._live_or_die_(i, j)) if self.data[i][j]==0 
                        else 'o' + str(self._live_or_die_(i, j)), 
                        sep='', end='\t')
            print('\n')

if __name__ == "__main__":
    grid = Grid(6)
    n = int(input("how many live cells at day0? (1 ~ 99) "))
    grid.create_the_world(n)
    grid.show()
    while True:
        grid.update()
        grid.show()
        cmd = input("n for next generation, q to quit: ")
        if cmd == 'q':
            break
