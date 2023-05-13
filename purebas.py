import uuid
import os

# definir una constante para el namespace de UUID
NAMESPACE_URL = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')

# leer el archivo de stop words
stop_words = []
with open('stopwords.txt', 'r') as f:
    stop_words = f.read().splitlines()

# obtener la oracion desde el usuario
sentence = input("Introduce una oración: ")

# separar la oracion en palabras y quitar las palabras irrelevantes
words_in_sentence = sentence.split()
words_in_sentence = [word for word in words_in_sentence if word.lower() not in stop_words]

# obtener los identificadores de cada palabra
word_ids = [str(uuid.uuid5(NAMESPACE_URL, str(word.lower()).encode('utf-8'))) for word in words_in_sentence]


# crear un diccionario con las relaciones entre las palabras
word_relations = {}
for i, word_id in enumerate(word_ids):
    for j, other_word_id in enumerate(word_ids):
        if i != j:
            if word_id not in word_relations:
                word_relations[word_id] = {}
            if other_word_id not in word_relations[word_id]:
                word_relations[word_id][other_word_id] = 0
            word_relations[word_id][other_word_id] += 1

# guardar la oracion en el archivo oraciones_DB
with open('oraciones_DB.txt', 'a') as f:
    f.write(sentence + '\n')

# guardar las palabras en el archivo palabras_DB
with open('palabras_DB.txt', 'a') as f:
    for word, word_id in zip(words_in_sentence, word_ids):
        f.write(f"{word_id} {word}\n")

# guardar las relaciones en el archivo relaciones_DB
with open('relaciones_DB.txt', 'a') as f:
    for word_id, other_word_ids in word_relations.items():
        for other_word_id, count in other_word_ids.items():
            f.write(f"{word_id} {other_word_id} {count}\n")