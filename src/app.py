# Libraries.
import pygame as pg
from src.cardioid import Cardioid
from src.ui import UI

# Initialize the libraries.
pg.font.init()


# App class to hold the main loop and window.
class App:
    # Constructor.
    def __init__(self) -> None:
        self.screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
        self.fullscreen = False
        self.clock = pg.time.Clock()
        self.cardioid = Cardioid(self)
        self.ui = UI(self)

    # Handle window resize event.
    def handle_resize(self, event) -> None:
        self.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
        self.cardioid.update_window_size(event.w, event.h)

    # Draw the window.
    def draw(self) -> None:
        self.screen.fill("black")
        self.cardioid.draw()
        self.ui.draw()
        pg.display.flip()

    # Run the main loop.
    def run(self) -> None:
        running = True

        # Main loop.
        while running:
            for event in pg.event.get():
                # Handle quit event.
                if event.type == pg.QUIT:
                    running = False

                # Handle window resize event.
                elif event.type == pg.VIDEORESIZE:
                    self.handle_resize(event)

            # Handle UI events.
            self.ui.handle_event(event)

            # Update the cardioid settings and draw.
            self.cardioid.update_settings(
                radius=self.ui.radius_slider.val, num_points=self.ui.points_slider.val
            )

            # Draw the window.
            self.draw()

            # Limit the frame rate.
            self.clock.tick(60)
        pg.quit()


# Check if the file is run directly.
if __name__ == "__main__":
    print("You can't run this file directly.")
