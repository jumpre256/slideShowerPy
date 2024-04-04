
def getSlides(path: str, splitter: str = ";") -> list:
	rawText = rawFileRead(path)
	data = rawText.split(splitter)
	if data[len(data)-1] == "":
		removeLast(data)
	return data

def removeLast(iterable) -> None:	#will edit the iterable passed in to this method.
	if len(iterable) > 0:
		iterable.pop(len(iterable)-1)

def rawFileRead(path: str) -> str:
	text = ""
	with open(path, "r") as file:
		text = file.read()
	return text
