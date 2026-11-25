import re

n, m = map(int, input().split())

dictionary = set()

for i in range(n):
    dictionary.add(input().lower())

text = ""

for i in range(m):
    text += input().lower() + " "

words = set(re.findall(r"[a-z]+", text))

if not words.issubset(dictionary):
    print("Some words from the text are unknown.")
elif not dictionary.issubset(words):
    print("The usage of the vocabulary is not perfect.")
else:
    print("Everything is going to be OK.")
