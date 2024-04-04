import pygame #SDL in the background. #will have text ready-to-use.

def main():
	prototype()

def prototype():
	#IntelliJ
	someData = ["1. Introduction.", "2. About atoms.", "3. Molecules",
	"4. Why you should care."]

	currentIndex = 0
	while True:
		usrInput = input(someData[currentIndex])
		if usrInput == "quit":
			quit()
		currentIndex = (currentIndex + 1) % len(someData)

if __name__ == "__main__":
	main()