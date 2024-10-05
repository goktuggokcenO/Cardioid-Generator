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
        self.counter = 0
        self.inc = 0.01

    # Update settings based on slider values.
    def update_settings(self, radius, num_points):
        self.radius = radius
        self.num_points = int(num_points)

    # Update window size and adjust cardioid position and radius.
    def update_window_size(self, width, height):
        # Keep the cardioid centered
        self.translate = (width // 2, height // 2)

        # Adjust the radius based on the smaller dimension (width or height)
        self.radius = min(width, height) // 2 - 50

    # Draw method.
    def draw(self):
        time = pg.time.get_ticks()
        factor = 1 + 0.0001 * time

        # Draw the cardioid.
        for i in range(self.num_points):
            theta = (2 * math.pi / self.num_points) * i

            x1 = int(self.radius * math.cos(theta)) + self.translate[0]
            y1 = int(self.radius * math.sin(theta)) + self.translate[1]
            x2 = int(self.radius * math.cos(factor * theta)) + self.translate[0]
            y2 = int(self.radius * math.sin(factor * theta)) + self.translate[1]
            pg.draw.line(self.app.screen, self.get_color(), (x1, y1), (x2, y2))

    # Get color method.
    def get_color(self):
        self.counter += self.inc
        if not (0 < self.counter < 1):
            self.counter = max(min(self.counter, 1), 0)
            self.inc *= -1
        return pg.Color("red").lerp("green", self.counter)


# Check if the file is being run directly.
if __name__ == "__main__":
    app = App()
    app.run()
