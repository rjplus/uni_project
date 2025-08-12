#!/usr/bin/env python
# coding: utf-8

# # API Interaction
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ## What is an API?
# - "Application programming interface"
# - A way for computer programs to interact with each other
# - Avoids manual work

# ![api-ui.drawio.svg](attachment:api-ui.drawio.svg)

# ## Web APIs
# - Our focus today
# - Alternative version of website
# - Pages contain machine-readable data instead of display-oriented HTML
# - Great for large datasets hosted elsewhere
# - Often based on "query"

# ## Example 1: Open Topo Data

# In[1]:


import requests

url = "https://api.opentopodata.org/v1/srtm90m"
data = {
    "locations": "-43.5,172.5",
    "interpolation": "cubic",
}
response = requests.post(url, json=data)


# In[2]:


print(response)


# In[3]:


data = response.json()  # a Python dictionary
print(data)


# In[4]:


results = data["results"]
print(results)


# In[5]:


elevation = results[0]["elevation"]
print(f"The altitude at the chosen spot is {elevation} metres")


# In[6]:


def get_elevation(latitude, longitude):
    url = "https://api.opentopodata.org/v1/srtm90m"
    data = {
        "locations": f"{latitude},{longitude}",
        "interpolation": "cubic",
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        data = response.json()
        results = data["results"]
        elevation = results[0]["elevation"]
        return elevation
    else:
        raise Exception("Invalid response from API. Check input.")


# In[7]:


print(get_elevation(-43.0, 172.3))
print(get_elevation(-43.5, 172.5))
print(get_elevation(-43.7, 172.1))


# In[8]:


print(get_elevation(-43.0, 380.0))


# In[9]:


try:
    height = get_elevation(-43.0, 380.0)
except:
    height = 0  # assume sea level if no data available
print(height)


# ## Example 2: TheCocktailDB

# In[10]:


import requests

ingredients_url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php"
data = {"i": "Galliano"}
response = requests.get(ingredients_url, params=data)


# In[11]:


response.status_code


# In[12]:


data = response.json()


# In[13]:


data


# In[14]:


[drink["strDrink"] for drink in data["drinks"]]


# In[15]:


drink_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
data = {"s": "Barracuda"}
response = requests.get(drink_url, params=data)


# In[16]:


response.status_code


# In[17]:


data = response.json()


# In[18]:


data


# In[19]:


cocktail = data["drinks"][0]
print(f'Make a {cocktail["strDrink"]} in a {cocktail["strGlass"]} using {cocktail["strIngredient1"]}')


# ## Summary
# - Access web APIs using the `requests` library
# - `requests.get` and `requests.post` for GET and POST requests
# - Use `.json()` to convert the response to a Python dictionary
# - Read the docs for the API you're using
# - Check status codes and throw exceptions

# ## Exercise
# Write a function that takes the name of an ingredient, and returns one recipe from TheCocktailDB that contains that ingredient.  The output string should be easy to read, and should list all ingredients along with the cocktail name and the instructions in English.

# ### Hints
# - Your function will need to do at least 2 API requests
# - You'll need to handle the case where the API returns no information
# - The ingredients are in the attributes `strIngredient1`, `strIngredient2` and so on.  Can you loop through these?

# ## Solution

# In[20]:


import requests

def get_recipe_with_ingredient(ingredient):
    ingredients_url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php"
    data = {"i": ingredient}
    response = requests.get(ingredients_url, params=data)
    data = response.json()
    name = data["drinks"][0]["strDrink"]
    
    drink_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
    data = {"s": "Barracuda"}
    response = requests.get(drink_url, params=data)
    data = response.json()
    cocktail = data["drinks"][0]
    
    ingredients = []
    i = 1
    while (ingredient := cocktail["strIngredient" + str(i)]) is not None:
        ingredients.append(ingredient)
        i += 1
    out = f'{cocktail["strDrink"]}: Uses {", ".join(ingredients)}. {cocktail["strInstructions"]}'
    return out

get_recipe_with_ingredient("Gin")

