import json
import requests
import time
import sys 

topic = "python"
MAIN_URL = "https://newsapi.org/v2/everything"

queryParams = {"apiKey": ""}
queryParams['q']= topic
queryParams['from']="2018-03-03"
queryParams['sortBy']="popularity"
queryParams['pageSize']=100

QUERY_PER_PAGE=100
STATUS_OK="200"
STATUS_NOTFINISHED={
 "500":"unknown reasons"
,"504":"gateway time out"
,"429":"too many requets in short time"
}

page_num=1

while(True):
       queryParams["page"]=page_num
       response = requests.get(url= MAIN_URL, params =queryParams )
       if(str(response.status_code) in STATUS_NOTFINISHED.keys()):
          time.sleep(5)
          print("sleeping for 5 seconds, because " + STATUS_NOTFINISHED[str(response.status_code)] )
        
       elif(str(response.status_code)==STATUS_OK):
          outfile=topic +"_"+str(page_num) +".txt"
          with open(outfile, 'w') as outfile:
             json.dump(response.json(), outfile)
          print("result "+ str(min(page_num*QUERY_PER_PAGE,int(response.json()['totalResults'])))+"/"+str(response.json()['totalResults'])+" traversed"  )
          if page_num*QUERY_PER_PAGE>=int(response.json()['totalResults']):
             print("travered finished") 
             sys.exit()

          page_num+=1	
          
       else:
           
          print("breaking wtih status code "+str(response.status_code)) 
          sys.exit()




