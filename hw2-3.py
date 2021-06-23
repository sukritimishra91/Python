import string

def poem(filepath):
	file_poem = {}
	with open(filepath) as fp:
		line = fp.readline()
		while line:
			line = fp.readline()
			new_line = "".join(c for c in line if c not in string.punctuation)
			new_line = new_line.strip()
			string_words = new_line.split()
			
			for word in string_words:
				length = len(word)
				if length in file_poem:
					if word in file_poem[length]:
						file_poem[length][word] += 1
					else:
						file_poem[length][word] = 1
				else:
					# create a new dictionary
					# add word to it
					newWord = {}
					newWord[word] = 1
					# add the above dictionary to length key
					# in main dictionary
					file_poem[length] = newWord
	sorted_poem = sorted(file_poem.items())
	for value in sorted_poem:
		length = value[0]
		dictionary = value[1]
		sorted_word_counts = sorted(dictionary.items(), key = lambda x: x[1], reverse=True)
		print(f'\n\nTop 15, length of word: {length}')
		cnt = 1
		for value in sorted_word_counts:
			if cnt <= 15:
				print(f'{value[0]} {value[1]}')
			else: 
				break
			cnt = cnt + 1

poem('sonnet.txt')
 