



def getSlides(path: str) -> list:
	rawText = "The dog (Canis familiaris or Canis lupus familiaris) is a domesticated descendant of the wolf. Also called the domestic dog, it is derived from extinct gray wolves, and the gray wolf is the dog's closest living relative. The dog was the first species to be domesticated by humans. Experts estimate that hunter-gatherers domesticated dogs more than 15,000 years ago, which was before the development of agriculture. Due to their long association with humans, dogs have expanded to a large number of domestic individuals and gained the ability to thrive on a starch-rich diet that would be inadequate for other canids."
	data = rawText.split(".")
	print(data[len(data)-1])
	if data[len(data)-1] == "":
		removeLast(data)
	return data

def removeLast(iterable) -> None:	#will edit the iterable passed in to this method.
	if len(iterable) > 0:
		iterable.pop(len(iterable)-1)

def rawFileRead(path: str) -> str:
	return ""

