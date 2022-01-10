import pygame
from PIL import Image, ImageSequence

def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(pilImage):
        frame = frame.convert('RGBA')
        pygameImage = pygame.image.fromstring(
            frame.tobytes(), frame.size, frame.mode).convert_alpha()
        frames.append(pygameImage)
    return frames
 
class AnimatedSpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, bottom, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom = (x, bottom))
        self.image_index = 0
    def update(self):
        self.image_index += 1
        self.image = self.images[self.image_index % len(self.images)]
        self.rect.x -= 5
        if self.rect.right < 0:
            self.rect.left = pygame.display.get_surface().get_width()

pygame.init()
window = pygame.display.set_mode((300, 200))
clock = pygame.time.Clock()
ground = window.get_height() * 3 // 4

gifFrameList = loadGIF('stone_age.gif')
animated_sprite = AnimatedSpriteObject(window.get_width() // 2, ground, gifFrameList)    
all_sprites = pygame.sprite.Group(animated_sprite)

run = True
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_sprites.update()

    window.fill((127, 192, 255), (0, 0, window.get_width(), ground))
    window.fill((255, 127, 64), (0, ground, window.get_width(), window.get_height() - ground))
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()