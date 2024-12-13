from collections import deque

printer_queue = deque()

## append is used as enque data to queue
printer_queue.append('resume.pdf')
printer_queue.append('Marketingnotes.docx')
printer_queue.append('proof.png')

while len(printer_queue) > 0:
    ## popleft is used as dequeue in queue
    document = printer_queue.popleft()
    print(document)
    