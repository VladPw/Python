s = str(input("Введіть речення: "))
words = s.split()
print("Слова з літерою 'о':")
for word in words:
    if "о" in word:
        print(word)