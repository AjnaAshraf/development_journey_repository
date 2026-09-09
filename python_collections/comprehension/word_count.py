words=["hello","hai","hello","hello","active","silent","wow"]

word_count = {w:words.count(w) for w in set(words)}

print(word_count)