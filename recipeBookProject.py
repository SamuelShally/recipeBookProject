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

    #gives more favorable ratings to strings that match from the beginning for a set prefix length
    #we want to put in a string, if it matches a recipe great! if not, return the index of the recipe
    #if not, then we have to find it
    def similar_substring(inputVal, lst):

        if (inputVal not in lst):
            for val in lst:
                if jaro.jaro_winkler_metric(inputVal, val) > .80 and jaro.jaro_winkler_metric(inputVal, val) < .99:
                    answer = input("Did you mean " + val + "? (y/n): ")
                    while answer not in ['y', 'n']:
                        answer = input("Did you mean " + val + "? (y/n): ")
                    if answer == 'y':
                        return val
                        break
                else:
                    

        else:
            return inputVal

    def view_all(recipe, recipe_name):
        print("Today we are cooking " + recipe[recipe_name]["name"])
        print(recipe[recipe_name]["description"])
        print("Ingredients")
        for val in recipe[recipe_name]["ingredient_list"]:
            print(val)

        print("Instructions")
        for val in recipe[recipe_name]["instructions"]:
            print(val)

    def view_step_by_step(recipe, recipe_name):
        print("Today we are cooking " + recipe[recipe_name]["name"])
        print(recipe[recipe_name]["description"])
        print("Ingredients")
        for val in recipe[recipe_name]["ingredient_list"]:
            print(val)
            input("Press enter to continue...")

        print("Instructions")
        for val in recipe[recipe_name]["instructions"]:
            print(val)
            input("Press enter to continue...")





    

add_recipe()
