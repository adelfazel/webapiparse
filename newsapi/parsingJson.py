import json
import os.path


stopwords= ["","[","]","at","as","a","the","is","that","with","of","in","to","an","and","for","on",
"was","by","be","it","which",")","from","there","had","how","have","has","this","","0","1"]
topic = "python"
summary=[]
QUERY_PER_PAGE=100
page_num=1
while(True):
    filename= topic + "_" + str(page_num) + ".txt"
    fileDir = os.getcwd()+"/"+filename
    if ((os.path.isfile(fileDir))==False):
       break
    else:
       data = json.load(open(filename))
       Docs = [doc for doc in data['articles']]
       for docIndex in range(len(Docs)):
          doc = Docs[docIndex]
          record_id = page_num*QUERY_PER_PAGE+docIndex+1
   
          headline =(doc['title']).lower().replace(","," ").replace("."," ").replace(";"," ")
          summary.append((record_id,headline,doc['publishedAt'][:10],doc['author']))
       page_num+=1 
    
for item in summary:
    print(item)



word_count = {}
for doc in summary:
    headline=doc[1]
    for word in headline.split(" "):
        if word in word_count:
           word_count[word]+=1
        else:
           word_count[word]=1
   
for word in stopwords:
    word_count.pop(word,None)

#for key, value in word_count.items():
#    print((key,value))



