import pygame #SDL in the background. #will have text ready-to-use.
import drawText
import textWrap
import getSlides

FPS = 60; WIDTH = 800; HEIGHT = 600
CAPTION = "slide shower.app"
version = "beta V1.1"
ANTIALIASING = True
PRE_FORMATTED = True
old_blue = (68, 227, 222)
bg_color = {False: (140, 212, 209), True: (52, 235, 110) }
FONT_SIZE = 45
LINE_GAP = 4

ENTRY_SPLITTER = "\n"
SLIDES_FILE_PATH = "data/questions01f.txt"
SLIDE_WRAP = False

def main():
    displayRun()

def displayRun() -> None:
    pygame.init()
    window = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption(CAPTION)
    drawText.window = window
    drawText.antialiasing = ANTIALIASING
    clock = pygame.time.Clock()

    slides = getSlides.getSlides(SLIDES_FILE_PATH, ENTRY_SPLITTER)
    slideIndex = 0

    progress = [False] * len(slides)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if SLIDE_WRAP:
                        slideIndex = (slideIndex + 1) % len(slides)
                    elif slideIndex < (len(slides) - 1):
                            slideIndex += 1
                if event.key == pygame.K_a:
                    if SLIDE_WRAP:
                        slideIndex = (slideIndex - 1) % len(slides)
                    elif slideIndex > 0:
                            slideIndex -= 1
                if event.key == pygame.K_z:
                    progress[slideIndex] = not progress[slideIndex]

        window.fill(bg_color[progress[slideIndex]])
        winWidth = window.get_size()[0]
        textObjects = textWrap.getTextObjects(winWidth, FONT_SIZE, slides[slideIndex], PRE_FORMATTED)
        i = 0
        for text in textObjects:
            h = (FONT_SIZE+LINE_GAP) * i
            drawText.draw_text_topleft(text, LINE_GAP+7, h, FONT_SIZE)
            i += 1
        pygame.display.update()
        clock.tick(FPS)

def prototype():
    testSlides = ["test"]
    currentIndex = 0
    while True:
        usrInput = input(testSlides[currentIndex])
        if usrInput == "quit":
            quit()
        currentIndex = (currentIndex + 1) % len(testSlides)

if __name__ == "__main__":
    main()