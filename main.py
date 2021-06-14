# Import libraries needed
import requests
import bs4

print('='*15)
print('PAGE 1 ONLY')
print('='*15)

# Get HTML text from the website
res = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup)

# Get the names of all the authors
authors=[]
author_class=soup.select('.author')
for auth in author_class:
  authors.append(auth.text)
print('\n'+'-'*15)
print('Authors')
print('-'*15)
print('\n'.join(authors))

# Get the list of the quotes
quotes=[]
quote_class=soup.select('.text')
for qt in quote_class:
  quotes.append(qt.text)
print('\n'+'-'*15)
print('Quotes')
print('-'*15)
print('\n'.join(quotes))

# Get the top 10 tags of the quotes
tags=[]
tags_count={}
tag_class=soup.select('.tag')
for tg in tag_class:
  tags.append(tg.text)

for cnt in set(tags):
  tags_count[cnt]=tags.count(cnt)

ranked_tag=list(sorted(tags_count.items(), key=lambda item: item[1],reverse=True))

print('\n'+'-'*15)
print('Top 10 Tags')
print('-'*15)
for tag in ranked_tag[:10]:
  print(tag[0])


print('\n'+'\n'+'='*15)
print('FIRST 10 PAGES')
print('='*15)
# Get HTML text from the website
authors_10page=[]

for i in range(1,11):
  res = requests.get(f"http://quotes.toscrape.com/page/{i}/")
  soup = bs4.BeautifulSoup(res.text, 'lxml')
  author_class=soup.select('.author')
  for auth in author_class:
    authors_10page.append(auth.text)

print('\n'+'-'*15)
print('Authors')
print('-'*15)
print('\n'.join(set(authors_10page)))


print('\n'+'\n'+'='*15)
print('ALL PAGES')
print('='*15)

page=1
all_authors=[]

while True:
  res = requests.get(f"http://quotes.toscrape.com/page/{page}/")
  soup = bs4.BeautifulSoup(res.text, 'lxml')

  if "No quotes found!" in soup:
    break

  author_class=soup.select('.author')
  for auth in author_class:
    all_authors.append(auth.text)
  page+=1

print('\n'+'-'*15)
print('Authors')
print('-'*15)
print('\n'.join(set(all_authors)))
