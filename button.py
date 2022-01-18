import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, button_size, label):
        super().__init__()

        self.size = button_size
        self.surf = pygame.Surface((self.size[0], self.size[1]))
        self.surf.fill((128, 128, 128))
        self.pos = pos
        self.rect = self.surf.get_rect(center = self.pos)

        self.label = label
        self.font = pygame.font.SysFont('arial', int(button_size[1]/2.5))
        self.button_label = self.font.render(self.label, True, (0, 0, 0))
        self.label_center = (self.button_label.get_width() / 2, self.button_label.get_height() / 2)
        self.label_pos = (self.pos[0] - self.label_center[0], self.pos[1] - self.label_center[1])

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        screen.blit(self.button_label, self.label_pos)
