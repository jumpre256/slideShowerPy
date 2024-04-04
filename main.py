import pygame #SDL in the background. #will have text ready-to-use.
import getSlides

FPS = 60; WIDTH = 800; HEIGHT = 600
ANTIALIASING = True

testData0 = ["1. Introduction.", "2. About atoms.", "3. Molecules",
    "4. Why you should care."]

def main():
    #print(getSlides.getSlides("testData/dogData.txt"))
    displayRun()

def displayRun() -> None:
    pygame.init()
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("client")
    clock = pygame.time.Clock()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.fill( (255, 255, 0) )
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