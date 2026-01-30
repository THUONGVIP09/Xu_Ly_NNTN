import requests
import re
from bs4 import BeautifulSoup
import underthesea

url='https://vnexpress.net/viet-nam-han-quoc-tran-chien-vi-danh-du-o-u23-chau-a-5009048.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

getdiv1=soup.find('section',{'class':'page-special-topic'})

getdiv2=soup.find('article',{'class':'fck_detail'})
getdiv3=getdiv2.find_all('p',{'class':'Normal'})
output=set()
for div in getdiv3:
    text = div.get_text(" ", strip=True)   
    output.add(text)
# ghi file
f = open("mytext.txt", "w", encoding="utf-8")  # w: write (ghi đè)
f.write("URL: " + url + "\n\n")
f.write("\n\n".join(output))
f.close()
output = {item.lower() for item in output}
output = {item.replace('\n', ' ') for item in output}
output = { re.sub(r'\d+', '', re.sub(r'[;<>{}"%,./()+\*?!…:-]','', item)) for item in output}
from underthesea import text_normalize, sent_tokenize, word_tokenize

output = {text_normalize(item) for item in output}
from pyvi import ViTokenizer
output = {tuple(ViTokenizer.tokenize(item).split()) for item in output}
from collections import Counter
tokens = []
for item in output:
    tokens.extend(list(item))   

freq = Counter(tokens)
for w, c in freq.most_common():
    print(f"{w} : {c}")


from langdetect import detect

text = " ".join(p.get_text(" ", strip=True) for p in getdiv3 if p.get_text(strip=True))
code = detect(text) 
detected_lang = "Tiếng Việt" if code == "vi" else ("Tiếng Anh" if code == "en" else code)

print("Ngôn ngữ bài viết:", detected_lang)

from underthesea import sent_tokenize

sentences = sent_tokenize(text)

print("Số câu:", len(sentences))

for s in sentences:
    print( s)
    print()   






    



