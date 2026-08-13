import requests
import json

#GET
params = {
    'limit': 3,
    'skips': 2
}
response = requests.get('https://dummyjson.com/products', params = params)

print(response.status_code)
print(json.dumps(response.json(), indent=4))

#POST
new_product = {'title': 'Midnight Library', 
               'price': 12}

response = requests.post('https://dummyjson.com/products/add', json=new_product)
print(response.status_code)
print(response.json()['id'])

product_id = response.json()['id']

#PUT
response = requests.put(f'https://dummyjson.com/products/{product_id}', json={'price': 15})
updated_product = response.json()
print(json.dumps(updated_product, indent=4))

#DELETE
response = requests.delete('https://dummyjson.com/products/2')
print(response.json()['isDeleted'])