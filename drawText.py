
#todo: dictionary of loaded sys fonts.
window = None

def draw_text_raw(w, text, x, y, size, maps,
    color = Color.black, sysFontName = "arial"):
        textFont = pygame.font.SysFont(sysFontName, size)
        textSurface = textFont.render(text, g.antialiasing, color)
        textRect = textSurface.get_rect()
        maps(textRect, x, y)
        window.blit(textSurface, textRect)

def draw_text_topleft(text, x, y, size,
    color = Color.black, sysFontName = "arial",):
        def map(rect, x, y):
            rect.topleft = (x,y)
        draw_text_raw(text, x, y, size, map,
            color, sysFontName)

def draw_text_center(g, text, x, y, size,
    color = Color.black, sysFontName = "arial"):
        def map(rect, x, y):
            rect.center = (x, y)
        draw_text_raw(text, x, y, size, map,
            color, sysFontName)