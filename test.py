import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"name": "Flask REST API", "views": 20000, "likes": 19928},
#        {"name": "Fast API with Python", "views": 50000, "likes": 49328},
#        {"name": "Fullstack project: React + Python", "views": 100000, "likes": 99958}]

#for i in range(len(data)):
#    response = requests.put(BASE + "video/" + str(i), data[i])
#    print(response.json())

response = requests.patch(BASE + "video/2", {"name": "Change video name", "likes": 0})
print(response.json())
