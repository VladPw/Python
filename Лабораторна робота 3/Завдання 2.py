word1 = input("Введіть перше слово: ")
while not word1.isalpha():
    word1 = input("Введіть ще раз, це має бути слово (не число): ")
word2 = input("Введіть друге слово: ")
while not word2.isalpha():
    word2 = input("Введіть ще раз, це має бути слово (не число): ")
found = False
print("Літери, що зустрічаються в обох словах лише один раз:")
for l in word1:
    if word1.count(l) == 1 and word2.count(l) == 1:
        print(l)
        found = True
if not found:
    print("Немає літер, які задовольняють умову.")
