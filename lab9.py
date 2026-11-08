import nltk
import string
import matplotlib.pyplot as plt

from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Завантаження необхідних ресурсів
nltk.download("gutenberg")
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

# Виведення списку текстів
print("Список текстів Project Gutenberg:")
print(gutenberg.fileids())

# Завантаження тексту відповідно до варіанта 7
text = gutenberg.raw("burgess-busterbrown.txt")

# Токенізація тексту
words = word_tokenize(text)

# Кількість слів
print("\nКількість слів у тексті:")
print(len(words))

# Кількість унікальних слів
unique_words = set(words)

print("\nКількість унікальних слів:")
print(len(unique_words))

# Порівняння кількості слів
print("\nПорівняння:")
print("Усього слів:", len(words))
print("Унікальних слів:", len(unique_words))

# Визначення 10 найбільш вживаних слів
fdist = FreqDist(words)
top_ten = fdist.most_common(10)

print("\n10 найбільш вживаних слів:")
print(top_ten)

# Побудова першої діаграми
plt.figure(figsize=(10, 5))

fdist.plot(10, title="10 найбільш вживаних слів у тексті")

plt.show()

# Видалення стоп-слів
stop_words = set(stopwords.words("english"))

without_stop_words = [
    word for word in words
    if word.lower() not in stop_words
]

# Видалення пунктуації
table = str.maketrans("", "", string.punctuation)

cleaned_words = [
    word.translate(table).lower()
    for word in without_stop_words
]

# Залишаємо тільки слова
cleaned_words = [
    word for word in cleaned_words
    if word.isalpha()
]

print("\nТекст після видалення стоп-слів і пунктуації:")
print(cleaned_words[:20])

# Визначення 10 найбільш вживаних слів після очищення
fdist_clean = FreqDist(cleaned_words)
top_clean = fdist_clean.most_common(10)

print("\n10 найбільш вживаних слів після очищення:")
print(top_clean)

# Побудова другої діаграми
plt.figure(figsize=(10, 5))

fdist_clean.plot(
    10,
    title="10 найбільш вживаних слів після очищення"
)

plt.show()

# Лематизація слів
lemmatizer = WordNetLemmatizer()

lemmatized_words = [
    lemmatizer.lemmatize(word)
    for word in cleaned_words
]

# Визначення 10 найбільш вживаних слів після лематизації
fdist_lemma = FreqDist(lemmatized_words)
top_lemma = fdist_lemma.most_common(10)

print("\n10 найбільш вживаних слів після лематизації:")
print(top_lemma)