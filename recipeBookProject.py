#creating the preliminary backend solution for the project
import pprint

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

    recipe_name = input("What is the recipe called?: \n")

    recipes[recipe_name] = {
                            "name" : recipe_name,
                            "description": "",
                            "ingredient_list": [],
                            "instructions" : []
                            }

    recipes[recipe_name]["description"] = input("Give a description of the dish: \n")

    anotherIngredient = "y"

    while(anotherIngredient == "y"):
        recipes[recipe_name]["ingredient_list"].append(input("Enter an ingredient: \n"))

        anotherIngredient = input("Would you like to enter another ingredient (y/n): ")

        # if anotherIngredient != "y" or anotherIngredient != "n":
        #     print("Please enter y or n, as one character")
        #     anotherIngredient = input("Would you like to enter another ingredient (y/n): ")




    anotherInstruction = "y"

    while (anotherInstruction == "y"):
        recipes[recipe_name]["instructions"].append(input("Enter an instruction: \n"))

        anotherInstruction = input("Would you like to enter another instruction (y/n): ")
        #
        # if anotherInstruction != "y" or anotherInstruction != "n":
        #     print("Please enter y or n, as one character")
        #     anotherInstruction = input("Would you like to enter another instruction (y/n): ")

    
    pprint.pprint(recipes)

    #given a string and list, returns the index of the string. If not, returns -1
    def exact_string_comparison(inputVal, lst):
        if(inputVal in lst):
            return lst.index(inputVal)
        else:
            return -1

    #same as exact string comparison, but not case sensitive
    def exact_string_ignore_case(inputVal, lst):
        lowerList = lst
        lowerList = [item.lower() for item in lowerList]

        if (inputVal in lowerList):
            return lowerList.index(inputVal)
        else:
            return -1


    

add_recipe()
