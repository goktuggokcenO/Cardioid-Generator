# Libraries.
import pygame as pg
import math


# Slider class with labels and modern design.
class Slider:
    def __init__(self, x, y, width, min_val, max_val, start_val, label):
        self.rect = pg.Rect(x, y, width, 20)  # Slider bar dimensions
        self.min_val = min_val
        self.max_val = max_val
        self.val = start_val
        self.grabbed = False
        self.label = label
        self.font = pg.font.SysFont(None, 24)  # Font for label

    def draw(self, screen):
        # Draw label on the left of the slider
        label_surf = self.font.render(self.label, True, (255, 255, 255))
        screen.blit(label_surf, (self.rect.x - 100, self.rect.y))

        # Draw slider background (track)
        pg.draw.rect(screen, (100, 100, 100), self.rect, border_radius=10)

        # Calculate the position of the handle
        pos = int(
            (self.val - self.min_val) / (self.max_val - self.min_val) * self.rect.width
        )

        # Draw the slider filled area
        pg.draw.rect(
            screen,
            (50, 205, 50),
            (self.rect.x, self.rect.y, pos, self.rect.height),
            border_radius=10,
        )

        # Draw the slider handle (circle)
        handle_x = self.rect.x + pos
        pg.draw.circle(
            screen, (255, 255, 255), (handle_x, self.rect.y + self.rect.height // 2), 10
        )

    def handle_event(self, event):
        # Handle slider interaction
        if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.grabbed = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.grabbed = False
        elif event.type == pg.MOUSEMOTION and self.grabbed:
            self.val = (event.pos[0] - self.rect.x) / self.rect.width * (
                self.max_val - self.min_val
            ) + self.min_val
            self.val = max(self.min_val, min(self.val, self.max_val))


# UI class to hold sliders.
class UI:
    def __init__(self, app):
        self.app = app
        # Sliders with labels
        self.radius_slider = Slider(120, 20, 200, 100, 400, 250, "Radius")
        self.points_slider = Slider(120, 60, 200, 50, 400, 200, "Points")

    def draw(self):
        self.radius_slider.draw(self.app.screen)
        self.points_slider.draw(self.app.screen)

    def handle_event(self, event):
        self.radius_slider.handle_event(event)
        self.points_slider.handle_event(event)


# App class to hold the main loop and window.
class App:
    # Constructor.
    def __init__(self):
        # Initialize libraries.
        pg.font.init()

        # Initialize the application.
        self.screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
        self.fullscreen = False
        self.clock = pg.time.Clock()
        self.cardioid = Cardioid(self)
        self.ui = UI(self)

    # Toggle fullscreen method.
    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            # Enter fullscreen mode
            self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        else:
            # Return to windowed mode
            self.screen = pg.display.set_mode((800, 600), pg.RESIZABLE)

    # Handle window resize event.
    def handle_resize(self, event):
        self.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
        self.cardioid.update_window_size(event.w, event.h)

    # Draw method.
    def draw(self):
        self.screen.fill("black")
        self.cardioid.draw()
        self.ui.draw()
        pg.display.flip()

    # Run method.
    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_f:  # Toggle fullscreen with 'F' key
                        self.toggle_fullscreen()
                elif event.type == pg.VIDEORESIZE:
                    self.handle_resize(event)  # Handle window resizing
                self.ui.handle_event(event)
            self.cardioid.update_settings(
                self.ui.radius_slider.val, self.ui.points_slider.val
            )
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
