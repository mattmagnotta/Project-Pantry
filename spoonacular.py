import requests

response = requests.get('https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,&apiKey=0c40f847c5b7496ba96549e08f60cf4b')


print(response.json())
