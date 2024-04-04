import pygame

#todo: dictionary of loaded sys fonts.
window = None
antialiasing = True

def draw_text_raw(text, x, y, size, maps,
    color = (0, 0, 0), sysFontName = "arial"):
        textFont = pygame.font.SysFont(sysFontName, size)
        textSurface = textFont.render(text, True, color)
        textRect = textSurface.get_rect()
        maps(textRect, x, y)
        window.blit(textSurface, textRect)

def draw_text_topleft(text, x, y, size,
    color = (0, 0, 0), sysFontName = "arial"):
        def map(rect, x, y):
            rect.topleft = (x,y)
        draw_text_raw(text, x, y, size, map,
            color, sysFontName)

def draw_text_center(text, x, y, size,
    color = (0, 0, 0), sysFontName = "arial"):
        def map(rect, x, y):
            rect.center = (x, y)
        draw_text_raw(text, x, y, size, map,
            color, sysFontName)