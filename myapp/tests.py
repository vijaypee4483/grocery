from django.test import TestCase
import json

# Create your tests here.
json_data = open('myapp/static/json/vegetables.json')
data = json.load(json_data)
json_data.close()
lst = data['vegetables']
num_veggies = lst['name']
num_instances = lst['availability']
print(num_veggies, num_instances)