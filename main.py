import pygame #SDL in the background. #will have text ready-to-use.
import drawText
import textWrap
import getSlides

FPS = 60; WIDTH = 800; HEIGHT = 600
ANTIALIASING = True
bg_color = (68, 227, 222)
FONT_SIZE = 45
LINE_GAP = 4

testData0 = ["1. Introduction.", "2. About atoms.", "3. Molecules",
    "4. Why you should care."]

def main():
    #print(getSlides.getSlides("testData/dogData.txt"))
    displayRun()

def displayRun() -> None:
    pygame.init()
    window = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("client")
    drawText.window = window
    drawText.antialiasing = ANTIALIASING
    clock = pygame.time.Clock()

    slides = getSlides.getSlides("testData/dogData.txt")
    slideIndex = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    #print("pressed d.")
                    slideIndex = (slideIndex + 1) % len(slides)

        window.fill(bg_color)
        winWidth = window.get_size()[0]
        textObjects = textWrap.getTextObjects(winWidth, FONT_SIZE, slides[slideIndex])
        i = 0
        for text in textObjects:
            h = (FONT_SIZE+LINE_GAP) * i
            drawText.draw_text_topleft(text, 0, h, FONT_SIZE)
            i += 1
        #drawText.draw_text_topleft(slides[slideIndex], 0, 0, FONT_SIZE)
        pygame.display.update()
        clock.tick(FPS)

def prototype():
    currentIndex = 0
    while True:
        usrInput = input(testData0[currentIndex])
        if usrInput == "quit":
            quit()
        currentIndex = (currentIndex + 1) % len(testData0)

if __name__ == "__main__":
    main()