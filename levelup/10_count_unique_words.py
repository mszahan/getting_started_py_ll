import re
from collections import Counter

## this function counts unique word from file
def count_words(path):
    with open(path, 'r', encoding='utf-8') as file:
        all_words = re.findall(r'[0-9a-zA-Z-]+', file.read())
        all_words = [word.upper() for word in all_words]
        print(f'\nTotal Words: {len(all_words)}')

        word_counts = Counter(all_words)

        print('\n Top 20 Words')
        for word in word_counts.most_common(20):
            print(f'{word[0]}\t{word[1]}')
        
count_words('shakespeare.txt')