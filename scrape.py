import pandas as pd
from bs4 import BeautifulSoup
import requests
import sys

url = sys.argv[1]
tag = sys.argv[2]
title = sys.argv[-1]
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

print(f'"url"; {url}'
      f'"tag": {tag}'
      f'"title": {title}')

tag_text_list = []

i = 1
for element in soup.find_all(tag):
    t = element.getText()
    tag_text_list.append({'tag_order': i, 'tag_text': t})
    i += 1


print(f'"total {tag} tags collected: {len(tag_text_list)}"')
df = pd.DataFrame(tag_text_list)
df.to_csv(f'{title}.csv')
print(f'file: ./{title}.csv')
