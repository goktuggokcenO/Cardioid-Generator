import pygame as pg
from src.cardioid import Cardioid
from src.ui.ui import UI

pg.font.init()


class App:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
        self.fullscreen = False
        self.clock = pg.time.Clock()
        self.cardioid = Cardioid(self)
        self.ui = UI(self)
        self.run()

    def handle_resize(self, event) -> None:
        self.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
        self.cardioid.update_window_size(event.w, event.h)

    def draw(self) -> None:
        self.screen.fill("black")
        self.cardioid.draw()
        self.ui.draw()
        pg.display.flip()

    def run(self) -> None:
        running = True

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
                radius=self.ui.radius_slider.val,
                num_points=self.ui.points_slider.val,
                color_speed=self.ui.color_slider.val,
            )

            # Draw the window.
            self.draw()

            # Limit the frame rate.
            self.clock.tick(60)
        pg.quit()


if __name__ == "__main__":
    print("You can't run this file directly.")
