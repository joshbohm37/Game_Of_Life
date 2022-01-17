import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, button_size, label):
        super().__init__()

        self.size = button_size
        self.surf = pygame.Surface((self.size[0], self.size[1]))
        self.surf.fill((255, 255, 255))
        self.pos = pos
        self.rect = self.surf.get_rect(center = self.pos)

        self.label = label
        self.font = pygame.font.SysFont('arial', button_size[1]//2)
        self.button_label = self.font.render(self.label, True, (128, 128, 128))

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        screen.blit(self.button_label, (self.pos[0] - (self.size[0]/2), self.pos[1] - (self.size[1]/2)))
