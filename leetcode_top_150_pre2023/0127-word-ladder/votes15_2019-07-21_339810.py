def gen_nei_word(word):
	for i in range(len(word)):
		for c in \'qwertyuiopasdfghjklzxcvbnm\':
			if c != word[i]: yield word[:i]+c+word[i+1:]
# yielded nei_word should be in wordList as well.