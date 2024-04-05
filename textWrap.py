
def getTextObjects(displayWidth, fontSize, text: str, preFormatted = False) -> list:
	if preFormatted == False:
		return __getTextObjects_nonPreformatted(displayWidth, fontSize, text)
	else:
		return __getTextObjects_preformatted(text)

def __getTextObjects_preformatted(text: str) -> list:
	return text.split("\\n")

def __getTextObjects_nonPreformatted(displayWidth, fontSize, text: str) -> list:
	#print("len(text)", len(text))
	charsPerLine = int(displayWidth//(fontSize*0.48)) - 1
	#print("charsPerLine", charsPerLine)
	textObjects = []
	words = text.split(" ")
	curWord = 0
	progress = 0
	while progress < len(text) and curWord <= (len(words) - 1):
		textObject = ""
		while True:
			#print("curWord", curWord)
			#print("progress", progress)
			if len(textObject + words[curWord]) > charsPerLine:
				break
			textObject += words[curWord] + " "
			curWord += 1
			if curWord > (len(words) - 1):
				break
		progress += len(textObject)
		if len(textObject) > 0:
			#print("len(textObject)", len(textObject))
			textObjects.append(textObject.strip())
	return textObjects
