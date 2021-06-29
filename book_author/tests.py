from django.test import TestCase

# Create your tests here.

import requests

url = 'http://127.0.0.1:8000/api/get_author'
data = {
    "Name":"西门吹雪",
    "Gender":1,
    "Born_Date":"2021-11-04"
}
resp = requests.post('http://127.0.0.1:8000/api/insert_author',data=data)


resp11 = requests.get('http://127.0.0.1:8000/api/author',params={ "Name":"西门吹雪"})



data1 = {"Author":"1","BookName":"三国演义","Publish_Date":"2021-11-04","Country":"1"}
data2 = {"BookName":"三国演义"}

resp12 = requests.post('http://127.0.0.1:8000/api/book',data=data1)
resp13 = requests.get('http://127.0.0.1:8000/api/book',params=data2)
