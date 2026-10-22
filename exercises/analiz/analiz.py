#количество строк;
#количество слов;
#количество уникальных слов;
#самое частое слово;
#самое длинное слово;
#количество знаков препинания.

word_count = {}
unique_words =set()

words_count = 0
lines_count = 0
punctuation_count = 0
longest_words = ""


import string

with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 1. Количество строк
lines = text.splitlines()
print("Количество строк:", len(lines))

# 2. Количество слов
words = text.split()
print("Количество слов:", len(words))

# Подготовим слова: уберём знаки препинания
clean_words = [
    word.strip(string.punctuation + ".,!?;:()«»—–")
    .lower()
    for word in words
]
clean_words = [word for word in clean_words if word]

# 3. Количество уникальных слов
unique_words = set(clean_words)
print("Уникальных слов:", len(unique_words))

# 4. Количество знаков препинания
punctuation_count = sum(
    1 for char in text if char in string.punctuation + ".,!?;:()«»—–"
)
print("Знаков препинания:", punctuation_count)

# 5. Самое длинное слово
longest_word = max(clean_words, key=len)
print("Самое длинное слово:", longest_word)

# 6. Самое часто встречающееся слово
word_count = {}

for word in clean_words:
    word_count[word] = word_count.get(word, 0) + 1

most_common_word = max(word_count, key=word_count.get)
print("Самое частое слово:", most_common_word)




