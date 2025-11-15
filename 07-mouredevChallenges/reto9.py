#HETEROGRAMA, ISOGRAMA, PANGRAMA

import re

def char_counter(text: str) -> dict[str,int]:
#def char_counter(text: str):
	no_number_text = re.sub(r"\d+", "", text.lower())
	no_punt_text = re.sub(r"[^\w\s]", "", no_number_text)

	char_counter = dict()
	#char_counter = {}

	for char in no_punt_text:
		if char in char_counter.keys():
			char_counter[char]+=1
		else:
			char_counter[char]=1
	return char_counter


def isHeterogram(text: str) -> bool:
	for counter in char_counter(text).values():
		if counter >1:
			return False
	return True

def isIsogram(text: str) -> bool:
	order=0
	#print("starting isIsogram..")
	for counter in char_counter(text).values():
		#print(counter)
		if order == 0:
			order=counter
		if order != counter:
			return False
	return True

def isPangram(text: str) -> bool:
	return len(char_counter(text).keys()) == 27

print("Heterogram")
word="luteranismos"
print(isHeterogram(word))

print("isogram")
word="intestines"
print(isIsogram(word))
