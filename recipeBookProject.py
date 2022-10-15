#creating the preliminary backend solution for the project
import pprint
import json
from os import path

filename = "data_storage.json"
objects = []

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
                            "Name" : recipe_name,
                            "Source" : "",
                            "Description": "",
                            "Ingredients": [],
                            "Instructions" : []
                            }

    recipes[recipe_name]["Description"] = input("Give a description of the dish: \n")

    anotherIngredient = "y"

    while(anotherIngredient == "y"):
        recipes[recipe_name]["Ingredients"].append(input("Enter an ingredient: \n"))

        anotherIngredient = input("Would you like to enter another ingredient (y/n): ")

        # if anotherIngredient != "y" or anotherIngredient != "n":
        #     print("Please enter y or n, as one character")
        #     anotherIngredient = input("Would you like to enter another ingredient (y/n): ")




    anotherInstruction = "y"

    while (anotherInstruction == "y"):
        recipes[recipe_name]["Instructions"].append(input("Enter an instruction: \n"))

        anotherInstruction = input("Would you like to enter another instruction (y/n): ")
        #
        # if anotherInstruction != "y" or anotherInstruction != "n":
        #     print("Please enter y or n, as one character")
        #     anotherInstruction = input("Would you like to enter another instruction (y/n): ")

    
    pprint.pprint(recipes)
    
    if path.isfile(filename) is False:
        raise Exception("That is not the correct file name!")
    
    with open(filename) as fp:
        objects = json.load(fp)
        
    print(objects)
    
    print(type(objects))
    
    objects.append(recipes)
    
    print(objects)
    
    
    with open(filename, "w") as outfile:
        json.dump(objects, outfile, indent=4, separators=(',',': '))

    print('Successfully appended to the JSON file')

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

        # if there is not an exact match already in there
        jaro_lst = []
        if (inputVal not in lst):
            for val in lst:
                curr_jaro  = jaro.jaro_winkler_metric(inputVal, val)
                jaro_lst.append(curr_jaro);
                
                if curr_jaro > .80 and curr_jaro < .99:
                    answer = input("Did you mean " + val + "? (y/n): ")
                    while answer not in ['y', 'n']:
                        print("Please enter either \'y\' or \'n\'")
                        answer = input("Did you mean " + val + "? (y/n): ")
                    if answer == 'y':
                        return lst.index(val)


            
            #if we exhaust the entire list and cannot find anything even close
            maxValInd = jaro_lst.index(max(jaro_lst))

            print("The closest match to what you have inputted is :", lst[maxValInd])

            secAnswer = input("Is that what you were looking for? (y/n): ")

            while secAnswer not in ['y', 'n']:
                print("Please enter either \'y\' or \'n\'")
                secAnswer = input("Is that what you were looking for? (y/n): ")

            if answer == 'y':
                return maxValInd

            else:
                print("Could not find any matches through substring match :(")
                return -1;

                    
        # if there is an exact match, you can just return that
        else:
            return lst.index(inputVal)

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
