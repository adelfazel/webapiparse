import json
import requests
import time
import sys 

topic = "engine"
MAIN_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

queryParams = {"api-key": ""}
queryParams['q']= topic
queryParams['begin_date']="18600101"
queryParams['end_date']="19000101"
queryParams['sort']="oldest"
queryParams['facet_field']={
"document_type": "article"

}
queryParams['facet_filter']=True

MAX_QUERYALOWED=5
STATUS_OK="200"
STATUS_NOTFINISHED={
 "500":"unknown reasons"
,"504":"gateway time out"
,"429":"too many requets in short time"

}

QUERY_PER_PAGE=10

def lastQueryDate(jData):
    lastDate =str(jData['response']['docs'][-1]['pub_date'][:10])
    print("updating pub date to " + lastDate)
    return (lastDate.replace("-",""))

queryRest=0
page_num=0
while(True):
    if (page_num==MAX_QUERYALOWED):
           if (len(response.json()['response']['docs'])==QUERY_PER_PAGE): 
              print("updating begin date in query parameters")
              queryParams['begin_date']=lastQueryDate(response.json())
              page_num=0
              queryRest+=1
           else:
              print("traversing finished breaking")
              sys.exit()
 
    while(page_num<MAX_QUERYALOWED):
       queryParams["page"]=page_num    
       response = requests.get(url= MAIN_URL, params =queryParams )
       if(str(response.status_code) in STATUS_NOTFINISHED.keys()):
          time.sleep(5)
          print("sleeping for 5 seconds, because " + STATUS_NOTFINISHED[str(response.status_code)] )
        
       elif(str(response.status_code)==STATUS_OK):
          outfile=topic +"_"+str(page_num+queryRest*MAX_QUERYALOWED) +".txt"
          with open(outfile, 'w') as outfile:
             json.dump(response.json(), outfile)
          print("page "+ str(page_num+queryRest*MAX_QUERYALOWED)+ " treavered all artciles until " + response.json()['response']['docs'][-1]['pub_date'][:10] + " visited" )
          page_num+=1	
       else:
           
          print("breaking wtih status code "+str(response.status_code)) 
          sys.exit()

