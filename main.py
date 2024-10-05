# Libraries.
import pygame as pg


# Application class.
class App:
    # Constructor.
    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        self.clock = pg.time.Clock()

    # Draw method.
    def draw(self):
        self.screen.fill("black")
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


# Check if the file is being run directly.
if __name__ == "__main__":
    app = App()
    app.run()
