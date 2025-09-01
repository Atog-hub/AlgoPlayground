import pygame as pg
pg.init()

BLUE = (0, 120, 215)
BLUE_HOVER = (0, 100, 180)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 1024, 576

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action=None):
        self.text = text
        self.rect = pg.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.font = pg.font.SysFont("Arial", 30)
        self.text_surf = self.font.render(text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        self.scale = 1.0
        self.target_scale = 1.0

    def draw(self, surface):
        mouse_pos = pg.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)

        # Set target scale based on hover
        self.target_scale = 1.05 if is_hovered else 1.0
        self.scale += (self.target_scale - self.scale) * 0.15 # Smooth animation

        if abs(self.scale - self.target_scale) < 0.001:
            self.scale = self.target_scale



        # Calculate scaled size and position
        scaled_width = int(self.rect.width * self.scale)
        scaled_height = int(self.rect.height * self.scale)
        offset_x = (self.rect.width - scaled_width) // 2
        offset_y = (self.rect.height - scaled_height) // 2

        scaled_rect = pg.Rect(
            self.rect.x + offset_x,
            self.rect.y + offset_y,
            scaled_width,
            scaled_height
        )

        # Choose color based on hover
        color = self.hover_color if is_hovered else self.color

        # Draw rounded rectangle
        pg.draw.rect(surface, color, scaled_rect, border_radius=15)

        # Draw text centered in the scaled rect
        text_rect = self.text_surf.get_rect(center=scaled_rect.center)
        surface.blit(self.text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos) and self.action:
                self.action()




