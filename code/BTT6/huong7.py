import json
from pyvi import ViTokenizer





input_file = "filtered_articles.json"


with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)
for item in data:
    content=item.get("content", "").strip()
    if content:
        token=ViTokenizer.tokenize(content)
        item["content_tokenized"]=token
    else:
        item["content_tokenized"]=""
with open(input_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4) 

        
