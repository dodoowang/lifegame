from pantograph import PantographHandler
from pantograph import SimplePantographApplication
import sys
from grid import Grid
import fire
import webbrowser


class GameOfLife(PantographHandler):

    def setup(self):
        size = self.settings.get("size", 10)
        pattern = self.settings.get("pattern", 40)
        self.grid = Grid(size, pattern)
        self.canvas_size = min(self.width, self.height) * 0.9

    def update(self):
        n = self.grid.size
        sz = self.canvas_size / n
        self.fill_rect(0, 0, n * sz, n * sz, "#113775")
        for i in range(n + 1):
            self.draw_line(0, i * sz, n * sz, i * sz, "#b8b8b8")
            self.draw_line(i * sz, 0, i * sz, n * sz, "#b8b8b8")
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if self.grid.data[i][j] == 1:
                    self.fill_rect(i * sz - sz,
                                   j * sz - sz,
                                   sz * .95,
                                   sz * .95,
                                   "#f49842")
        self.grid.update()

    def on_close(self):
        print("web socket closed by client.")
        sys.exit(0)


def ShowOnWeb(n=10, day0=40, fps=10):
    app = SimplePantographApplication(GameOfLife,
                                      size=n, pattern=day0,
                                      timer_interval=1000//fps)
    webbrowser.open_new_tab("http://127.0.0.1:8080")
    app.run()


if __name__ == "__main__":
    fire.Fire(ShowOnWeb)
