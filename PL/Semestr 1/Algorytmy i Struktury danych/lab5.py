import requests
from bs4 import BeautifulSoup
import re
import random

#Zadanie 1
print(f'Zadanie 1:')
url = "https://www.gutenberg.org/cache/epub/11/pg11.txt"
response = requests.get(url)
text = response.text

def count_words(text):
    words_count = {}
    words = re.findall(r'\b\w+\b', text.lower())
    
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
            
    return words_count

def top_words(words_count):
    sorted_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words[:10]:
        print(f'{word}: {count}')

word_counts = count_words(text)
top_words(word_counts)

#Zadanie 2
print(f'Zadanie 2:')
def collatz_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def find_longest_collatz(limit):
    max_length, starting_number = 0, 0

    for i in range(1, limit):
        current_length = collatz_length(i)
        if current_length > max_length:
            max_length = current_length
            starting_number = i

    return starting_number

result = find_longest_collatz(1000000)
print(result)

#Zadanie 3
print(f'Zadanie 3:')
def djb2(key):
    hash_value = 5381
    for char in key:
        hash_value = (hash_value * 33) ^ ord(char)
    return hash_value

def find_collision(target_hash):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    length = 10

    while True:
        random_combination = ''.join(random.choices(alphabet, k=length))
        hash_value = djb2(random_combination) % 997

        if hash_value == target_hash:
            return random_combination

collision_result = find_collision(42)
print(collision_result)

#Zadanie 4
print(f'Zadanie 4:')
def retrieve(hash_table, key):
    idx = djb2(key) % len(hash_table)

    if hash_table[idx] and hash_table[idx][0] == key:
        return hash_table[idx][1]

    for idx in range(len(hash_table)):
        if not hash_table[idx]:
            return None

        if hash_table[idx][0] == key:
            return hash_table[idx][1]

    print("Error: Key not found.")
    return None

hash_table = [None] * 1000  # Example hash table
key_to_find = 'example_key'
value_assigned = 'example_value'
hash_table[djb2(key_to_find) % len(hash_table)] = (key_to_find, value_assigned)

result = retrieve(hash_table, key_to_find)
print(result)
