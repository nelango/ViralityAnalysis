import requests
import json
from elasticsearch import Elasticsearch

#  ES instance
# es = Elasticsearch()
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# hit localhost sw database
# res = requests.get('http://localhost:9200')
# print(res.content)
# r = requests.get('http://localhost:9200') 
# i = 1
# while r.status_code == 200:
#     r = requests.get('http://swapi.co/api/people/'+ str(i))
#     es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
#     i=i+1
# print(i)

# database fetch
res = es.get(index='sw', doc_type='people', id=5)
# parsed = json.loads(res)
# print json.dumps(parsed, indent=4, sort_keys=True)
print(json.dumps(res,indent=4, sort_keys=True))
# type(res)
# print(" response: '%s'" % (res))
# print("results:")
# print("Got %d Hits" % res['hits']['total'])
# for hit in res['hits']['hits']:
# 	print(hit["_source"])

