sentence = "i love eating burger"
searchWord = "burg"

def ispre(x):
	if x[:len(searchWord)] == searchWord:
		return True

for i in range(len(sentence.split())):
	if ispre(sentence.split()[i]):
			print(i + 1)
				break