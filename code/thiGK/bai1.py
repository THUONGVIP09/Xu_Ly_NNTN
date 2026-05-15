
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
import requests
import re
doc='Thông tin tuyển sinh nghành <a href="http://udn.vn/cntt.html">Công nghệ thông tin</a>. Liên hệ Tư vấn <a href="http://udn.vn/contact.php">tại đây</a> hoặc SĐT <b>0123456789</b>.'
soup1=BeautifulSoup(doc)
#tìm URL
url=re.findall(r'href=[\'"]?(https?://[^\'" >]+)[\'"]?',doc)
print(url)
#xóa thẻ HTML
th=re.sub(r'<[^>]+>','',doc)
print(th)

#tách câu
print("tách văn bản thành các câu:")
print(sent_tokenize(doc))


    