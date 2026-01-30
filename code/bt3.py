import requests
import re
from bs4 import BeautifulSoup
#bai1
url='http://forum.ehou.edu.vn/index.php?threads/chia-s%E1%BA%BB-t%C3%A0i-li%E1%BB%87u-h%E1%BB%8Dc-t%E1%BA%ADp-cho-m%E1%BB%8Di-ng%C6%B0%E1%BB%9Di.2556/page-2'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
getdiv1=soup.find('form',{'class':'InlineModForm section'})
getdiv2=getdiv1.find_all('li',{'class':'message'})
output=set()
file=open("output_bai1.txt","w",encoding="utf-8")
for div in getdiv2:
    text = div.get_text(" ", strip=True)   
    output.add(text)
for item in output:

    email=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    item1=re.findall(email,item)
    if item1:
        print(item1)
        file.write(str(item1)+"\n")

   
    phone=r'[(\+84|0)\d]{9,10}'
    item2=re.findall(phone,item)
    if item2:
        print(item2)
        file.write(str(item2)+"\n")
    
file.close()
#bai2

url1='https://vietnamnet.vn/ngoi-lang-dam-chat-tho-cach-ha-noi-200km-chup-anh-dep-mien-che-2484938.html'
response1 = requests.get(url1)
soup1 = BeautifulSoup(response1.content, 'html.parser')
getdiv4=soup1.find('div',{'class':'maincontent main-content'})
getp=getdiv4.find_all('p')

file1=open("output_bai2.txt","w",encoding="utf-8")
file2=open("Hà_Nội.txt","w",encoding="utf-8")
output1=set()
import underthesea
from underthesea import text_normalize, sent_tokenize, word_tokenize

for p in getp:
    text = p.getText()   
    output1.add(text)
print(output1)
sent=[]
word=[]
from pyvi import ViTokenizer
for item in output1:
    sentences = sent_tokenize(item)
  
    for s in sentences:
        sent.append(s)
        file1.write(s+"\n")

    words=ViTokenizer.tokenize(item).split()
    for w in words:
        word.append(w)
        ghep=r'^[A-Z]+[\w_]+(?:_[\w_]+)+'
        timtughep=re.findall(ghep,w)
        if timtughep:
            print(timtughep)
            file2.write(str(timtughep)+"\n")
file1.close()
file2.close()





