'''
process_quotes.py

by rad1osketxh

turns a text file of quotes into a javascript array
each quote must be delimited by a double newline: '\n\n'
'''

file = open('quotes.txt', encoding='utf-8')
quotes = file.read()

array = quotes.split('\n\n')

with open('quotes.js', 'w') as f:
    f.write('export const quotes =[\n')
    for item in array:
        item = item.strip().replace("\n", '\\\n').replace('"', "'")
        f.write(f'  "{item}",\n')
    f.write('];\n')