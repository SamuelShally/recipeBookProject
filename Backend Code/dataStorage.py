#creating the preliminary backend solution for the project

def add_recipe():
    # we will be using dictionaries as the storage method of choice
    recipes = {}
    # { "recipe_name" : {
        #str "name" : str [string of name],
        #str "description" : str [description]
        #str "ingredient list" : arr [ingredients, ingredients,...]
        #str "step by step instructions" : arr [instruction, instruction, instruction]
    #   }
    # }

    recipe_name = input("What is the recipe called?")

    recipes[recipe_name] = {
                            "name" : "",
                            "description": "",
                            "ingredient_list": [],
                            "instructions" : []
                            }

    