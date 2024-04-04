
def getTextObjects(displayWidth, fontSize, text: str, preFormatted = False) -> list:
	if preFormatted == False:
		return __getTextObjects_nonPreformatted(displayWidth, fontSize, text)
	else:
		return __getTextObjects_preformatted(text)

def __getTextObjects_preformatted(text: str) -> list:
	return text.split("\\n")

def __getTextObjects_nonPreformatted(displayWidth, fontSize, text: str) -> list:
	charsPerLine = int(displayWidth//(fontSize*0.48))
	#print("charsPerLine", charsPerLine)
	textObjects = []
	lastChar = " "
	i = 0
	while i < len(text):
		#print("lastChar", lastChar)
		textPiece = text[i:i+charsPerLine]
		textPrepend = ""
		if lastChar != " " and textPiece[0] != " ":
			textPrepend = "-"
		textPiece = textPrepend + textPiece
		lastChar = textPiece[len(textPiece) - 1]
		textObjects.append(textPiece)
		i += charsPerLine
	return textObjects