# Libraries.
import pygame as pg
import math


# Cardioid class.
class Cardioid:
    # Constructor.
    def __init__(self, app) -> None:
        self.app = app
        self.radius = 250
        self.num_points = 200
        self.translate = (
            self.app.screen.get_width() // 2,
            self.app.screen.get_height() // 2,
        )
        self.counter = 0
        self.color_speed = 0.01
        self.factor_change = 0.0001

    # Update settings based on slider values.
    def update_settings(self, radius, num_points, color_speed, factor_change) -> None:
        self.radius = radius
        self.num_points = int(num_points)
        self.color_speed = color_speed
        self.factor_change = factor_change

    # Update window size and adjust cardioid position and radius.
    def update_window_size(self, width, height) -> None:
        # Keep the cardioid centered
        self.translate = (width // 2, height // 2)

        # Adjust the radius based on the smaller dimension (width or height)
        self.radius = min(width, height) // 2 - 50

    # Get color method.
    def get_color(self) -> pg.Color:
        self.counter += self.color_speed
        if not (0 < self.counter < 1):
            self.counter = max(min(self.counter, 1), 0)
            self.color_speed *= -1
        return pg.Color("red").lerp("green", self.counter)

    # Draw method.
    def draw(self) -> None:
        time = pg.time.get_ticks()
        factor = 1 + self.factor_change * time

        # Draw the cardioid.
        for i in range(self.num_points):
            theta = (2 * math.pi / self.num_points) * i
            x1 = int(self.radius * math.cos(theta)) + self.translate[0]
            y1 = int(self.radius * math.sin(theta)) + self.translate[1]
            x2 = int(self.radius * math.cos(factor * theta)) + self.translate[0]
            y2 = int(self.radius * math.sin(factor * theta)) + self.translate[1]
            pg.draw.line(self.app.screen, self.get_color(), (x1, y1), (x2, y2))


# Check if the file is run directly.
if __name__ == "__main__":
    print("You can't run this file directly.")
