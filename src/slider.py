# Libraries.
import pygame as pg


# Slider class to hold slider properties and design.
class Slider:
    # Constructor.
    def __init__(self, x, y, width, min_val, max_val, start_val, label) -> None:
        self.rect = pg.Rect(x, y, width, 20)
        self.min_val = min_val
        self.max_val = max_val
        self.val = start_val
        self.grabbed = False
        self.label = label
        self.font = pg.font.SysFont(None, 24)  # Font for label

    # Draw method.
    def draw(self, screen) -> None:
        # Draw label on the left of the slider.
        label_slider = self.font.render(self.label, True, "white")
        screen.blit(label_slider, (self.rect.x - 100, self.rect.y))

        # Draw slider background.
        pg.draw.rect(
            surface=screen, color=(100, 100, 100), rect=self.rect, border_radius=10
        )

        # Calculate the position of the handle.
        handle_pos = int(
            (self.val - self.min_val) / (self.max_val - self.min_val) * self.rect.width
        )

        # Draw the slider filled area
        pg.draw.rect(
            surface=screen,
            color=(50, 205, 50),
            rect=(self.rect.x, self.rect.y, handle_pos, self.rect.height),
            border_radius=10,
        )

        # Draw the slider handle (circle)
        handle_x = self.rect.x + handle_pos
        pg.draw.circle(
            surface=screen,
            color=(255, 255, 255),
            center=(handle_x, self.rect.y + self.rect.height // 2),
            radius=10,
        )

    # Handle slider interaction.
    def handle_event(self, event) -> None:
        # Check if the mouse button is pressed down inside the slider area
        if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.grabbed = True

        # Release the slider grab when the mouse button is released
        if event.type == pg.MOUSEBUTTONUP:
            self.grabbed = False

        # Update the slider value if grabbed and the mouse is moving
        if event.type == pg.MOUSEMOTION and self.grabbed:
            # Directly check if the mouse button is still pressed during motion
            if not pg.mouse.get_pressed()[0]:
                self.grabbed = False
                return
            
            # Calculate and lock the handle movement within the slider range
            self.val = (event.pos[0] - self.rect.x) / self.rect.width * (
                self.max_val - self.min_val
            ) + self.min_val

            # Clamp the value within the slider's range
            self.val = max(self.min_val, min(self.val, self.max_val))



# Check if the file is run directly.
if __name__ == "__main__":
    print("You can't run this file directly.")
