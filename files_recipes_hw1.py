#cook_book = {
#  'Омлет': [
#    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#    ],

cook_book = {}

with open ('recipes.txt', 'r') as file:
    lines = file.readlines() #list
    while '\n' in lines:
        lines.remove('\n')

    index_counter = 0
    while index_counter < len(lines):
        dish_key = lines[index_counter][0:-1]
        cook_book[dish_key] = []
        index_counter += 1

        n_dishes = int(lines[index_counter][0])
        for ingridient_loop in range(n_dishes):
            index_counter += 1
            
            lines[index_counter].split(' | ')
            ingredient_list = lines[index_counter].split(' | ')
            
            new_dict = {}
            new_dict['ingredient_name'] = ingredient_list[0]
            new_dict['quantity'] = ingredient_list[1]
            new_dict['measure'] = ingredient_list[2][0:-1]
            
        
            cook_book[dish_key].append( new_dict)
        index_counter += 1



# task 2

def get_shop_list(dish_list, n_persons):
    all_ingredients = []  
    for dish in dish_list:
        all_ingredients += cook_book[dish]
        
    all_ingredients_dict = {}
    for ingredient in all_ingredients:
        
        ingredient_copy = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity'])*n_persons}

        if ingredient['ingredient_name'] in all_ingredients_dict:
            base_ingridient = all_ingredients_dict[ingredient['ingredient_name']]
            base_ingridient['quantity'] += ingredient_copy['quantity']
            all_ingredients_dict[ingredient['ingredient_name']] = base_ingridient
        else:
            all_ingredients_dict[ingredient['ingredient_name']] = ingredient_copy
    return all_ingredients_dict 

#  {'ingredient_name' : 'Картофель', 'measure': 'кг', 'quantity': 2}
#  'Картофель': {'measure': 'кг', 'quantity': 2}

print( get_shop_list(["Омлет", "Омлет"], 3) )






  
