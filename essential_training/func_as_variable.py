text = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
'''

def lowercase(text):
    return text.lower()

def remove_punc(text):
    punctuations = ['.', '-', ',', '*']
    for puntuation in punctuations:
        text = text.replace(puntuation, '')
    return text

def remove_new_lines(text):
    text = text.replace('\n', '')
    return text

def remove_short_words(text):
    return ' '.join([word for word in text.split() if len(word) > 3])

def remove_long_words(text):
    return ' '.join([word for word in text.split() if len(word) < 6])

processing_functions = [lowercase, remove_punc, remove_new_lines, remove_short_words]

for func in processing_functions:
    text = func(text)

# print(text)


#lambda function

# defining and calling in the single line
print((lambda x:x+3)(5))

