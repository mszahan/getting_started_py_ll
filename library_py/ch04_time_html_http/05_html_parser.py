from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start tag: ', tag)
        for attr in attrs:
            print('attr:', attr)
    
    def handle_endtag(self, tag):
        print('End Tag', tag)
    def handle_comment(self, data):
        print('Comment: ', data)
    def handle_data(self, data):
        print('Data:', data)

parser = HTMLParser()
html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>This is title</title>
</head>
<body>
    <h1> Hello dear </h1>
</body>
</html>

'''
parser.feed(html)
# print()


## parsing html file

htmlfile = open('parser.html', 'r')
s = ''
for line in htmlfile:
    s+= line

parser.feed(s)
