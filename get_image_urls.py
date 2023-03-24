'''
get_image_urls.py

by rad1osketxh

based on https://serpapi.com/blog/scrape-google-images-with-python/
'''
import os
import requests, re, json, urllib.request
from bs4 import BeautifulSoup
from tqdm import tqdm

os.system('del image_urls.js')

headers = {
    # https://www.whatismybrowser.com/detect/what-is-my-user-agent/?ref=serpapi.com
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'
}

with open('image_urls.js', 'a') as f:
    f.write('export var urls = [\n')

for query in [
    'spirit halloween',
    'shadow wizard money gang',
    'shadow government',
    'gmod nuke',
    'lean gang',
    '420 mlg',
    '420 mlg background',
    'mlg peter griffin',
    'badass skeleton meme',
    'gangster spongebob',
    'john cena mlg',
    'instagram model quotes',
    'instagram model',
    'bby goyard',
    'bby goyard art',
    'bby goyard shannon',
    'scenecore aesthetic',
    'corrupted aesthetic',
    'corrupted aesthetic anime',
    'gothcore goku',
    'gothcore cartoons',
    'gothcore cartoons pastel goth',
    'clowncore',
    'goth clowncore',
    'anime clowncore',
    'roblox clowncore',
    'fesh pince',
    'ytp',
    'ytp sexer',
    'gurgi',
    'gurgi plushie',
    'cursed crochet',
    'cursed dollmaking',
    'terrible crochet pokemon',
    'spiderman 2',
    'pokemon',
    'lesbian',
    'north korean war propaganda',
    'funny minecraft memes',
    'hillary clinton',
    'finfin',
    'gru minions',
    'minion meme',
    'homestuck',
    'faygo',
    'gamzee makara',
    'insane clown possee',
    'guy fieri',
    'dancing polish cow',
    'legend of zelda meme',
    'ocarina of time meme',
    'sussy baka',
    'when the impostor is sus',
    'jerma',
    'the worst image on the internet',
    'kim jong un',
    'griffin mcelroy',
    'wayneradio funny',
    'sheen jimmy neutron',
    'autism creature',
    'hatsune miku lesbian',
    'peter griffin crack',
    'stewie griffin gangster',
    'gumball gangster',
    'wizard 101 memes',
    'breaking bad meme',
    'goku reaction image',
    'spongebob stupid faces',
    'thomas dale high school',
    'SCAD']:
    print('\n\nSearching for', query, '\n')

    params = {
        'q': query,
        'tbm': 'isch',
        'hl': 'en',
        'gl': 'us',
        'ijn': '0'
    }
    
    html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, "lxml")

    # Get images with request headers
    del params['ijn']
    params['content-type'] = 'image/png'

    image_urls = []
    for img in tqdm(soup.select('img')):
        # print(img['jsname'])
        for key in ['src', 'data-src']:
            try:
                url = img[key]
                for disqualifier in ['menu', 'data:image', 'fonts', 'logos', 'favicon']:
                    if disqualifier in url.lower():
                        raise KeyError
                image_urls.append(url)
            except KeyError:
                pass

    with open('image_urls.js', 'a') as f:
        print('Writing to file...')
        for url in tqdm(image_urls):
            f.write(f'\"{url}\",\n')
        f.close()

with open('image_urls.js', 'a') as f:
    f.write('];')

with open('image_urls.js', 'r') as f:
    urls = f.read()
    print('Total Urls:', len(urls.split('\n')))
    f.close()
