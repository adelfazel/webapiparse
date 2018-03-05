import json
import os.path


stopwords= ["","[","]","at","as","a","the","is","that","with","of","in","to","an","and","for","on","was","by","be","it","which",")","from","there","had","have","has","this",""]
topic = "engine"
summary=[]
page_num=0
while(True):
    filename= topic + "_" + str(page_num) + ".txt"
    fileDir = os.getcwd()+"/"+filename
    if ((os.path.isfile(fileDir))==False):
       break
    else:
       data = json.load(open(filename))
       Docs = [doc for doc in data['response']['docs']]
       for docIndex in range(len(Docs)):
          doc = Docs[docIndex]
          record_id = page_num*10+docIndex+1
                   
          headline =(doc['headline']['main'] +" " + doc['snippet']).lower().replace(","," ").replace("."," ").replace(";"," ")
          summary.append((record_id,headline,doc['word_count'],doc['pub_date'][:10]))
       page_num+=1 
    
#for item in summary:
#    print(item)



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

for key, value in word_count.items():
    print((key,value))



