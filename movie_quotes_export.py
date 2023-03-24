import os
import re
from tqdm import tqdm

os.system('del movie_quotes.js')

quotes = []

pattern = re.compile('[A-Z][a-z]')

for movie in os.listdir('./movie_scripts'):
    with open('./movie_scripts/' + movie, 'r') as f:
        script = f.read()
        lines = script.split('\n\n')
        for line in tqdm(lines):
            line = line.strip(' \t\n')
            line = line.replace('\n', '')
            line = line.replace('"', "'")
            if pattern.match(line[:2]):
                quotes.append(line)

print(quotes[:10])

with open('movie_quotes.js', 'w') as f:
    f.write('export var quotes = [\n')
    for line in tqdm(quotes):
        f.write(f'"{line}",\n')
    f.write('];')