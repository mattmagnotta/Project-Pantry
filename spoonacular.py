import requests
import json
import .


from .secrets import spoonacular_api_key
response = requests.get('https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,&apiKey=0c40f847c5b7496ba96549e08f60cf4b')
# json_data = json.loads(response.text)
#
# print(json_data)
# for i in range(len(json_data)):
#     id = json_data[i]["title"]
#     i += 1
#     print(id)

recipes = json.loads(response.text)
for i in range(len(recipes)):
    recipe_id = recipes[i]["id"]
    name = recipes[i]["title"]
    print(name)


response = requests.get('https://api.spoonacular.com/recipes/random?number=1')
