# Libraries.
from src.slider import Slider


# UI class to hold ui elements.
class UI:
    # Constructor.
    def __init__(self, app) -> None:
        self.app = app

        # Create rasius slider.
        self.radius_slider = Slider(
            x=120,
            y=20,
            width=200,
            min_val=100,
            max_val=400,
            start_val=250,
            label="Radius",
        )

        # Create number of points slider.
        self.points_slider = Slider(
            x=120,
            y=60,
            width=200,
            min_val=50,
            max_val=400,
            start_val=200,
            label="Points",
        )

    # Draw method.
    def draw(self) -> None:
        self.radius_slider.draw(self.app.screen)
        self.points_slider.draw(self.app.screen)

    # Handle event method.
    def handle_event(self, event) -> None:
        self.radius_slider.handle_event(event)
        self.points_slider.handle_event(event)


# Check if the file is run directly.
if __name__ == "__main__":
    print("You can't run this file directly.")
