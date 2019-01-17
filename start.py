import requests
from elasticsearch import Elasticsearch
import json

def init():
    res = requests.get('http://localhost:9200')
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    r = requests.get('http://localhost:9200') 
    i = 1
    while r.status_code == 200:
        r = requests.get('http://swapi.co/api/people/'+ str(i))
        es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
        i=i+1
    
    #print(es.get(index='sw', doc_type='people', id=5))
    print(es.search(index="sw", body={"query": {"prefix" : { "name" : "lu" }}}))

if __name__ == "__main__":
    init()
