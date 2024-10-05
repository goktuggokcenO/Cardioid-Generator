# Libraries.
import pygame as pg
import math


# Application class.
class App:
    # Constructor.
    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        self.clock = pg.time.Clock()
        self.cardioid = Cardioid(self)

    # Draw method.
    def draw(self):
        self.screen.fill("black")
        self.cardioid.draw()
        pg.display.flip()

    # Run method.
    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.draw()
            self.clock.tick(60)
        pg.quit()


# Cardioid class.
class Cardioid:
    # Constructor.
    def __init__(self, app):
        self.app = app
        self.radius = 250
        self.num_points = 200
        self.translate = (
            self.app.screen.get_width() // 2,
            self.app.screen.get_height() // 2,
        )

    # Draw method.
    def draw(self):
        for i in range(self.num_points):
            theta = (2 * math.pi / self.num_points) * i

            x1 = int(self.radius * math.cos(theta)) + self.translate[0]
            y1 = int(self.radius * math.sin(theta)) + self.translate[1]

            x2 = int(self.radius * math.cos(2 * theta)) + self.translate[0]
            y2 = int(self.radius * math.sin(2 * theta)) + self.translate[1]

            pg.draw.line(self.app.screen, "green", (x1, y1), (x2, y2))


# Check if the file is being run directly.
if __name__ == "__main__":
    app = App()
    app.run()
