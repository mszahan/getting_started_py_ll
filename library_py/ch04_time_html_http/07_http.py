from urllib import request
import json
import textwrap


with request.urlopen('https://www.googleapis.com/books/v1/volumes?q=:1101904224') as f:
    text = f.read()
    decodedtext = text.decode('utf-8')
    print(textwrap.fill(decodedtext, width=50))

print()

obj = json.loads(decodedtext)
print(obj['kind'])

print(obj['items'][0]['searchInfo']['textSnippet'])
