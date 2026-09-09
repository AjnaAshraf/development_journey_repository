"""
q2)words=["hai","hello","hai","hai","hai"]

    write a program to print word count
"""
words=["hai","hello","hai","hai","hai"]

words_set =set(words)

word_cnt = {}

for word in words_set:

    word_cnt[word]=words.count(word)

print(word_cnt)