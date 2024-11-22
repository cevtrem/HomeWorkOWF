cook_book = {}
ingredient = {}

with open('recipes.txt', 'r') as file:
    text = file.read()
    list_dishes = text.split('\n\n')
    amount_dishes = len(list_dishes)
    for dish in list_dishes:
        list_ingredients = []
        name_dish = dish.split('\n')[0]
        quantity_ingredients = int(dish.split('\n')[1])
        dish_line = dish.split('\n')
        for line in dish_line:
            if '|' in line:
                list_line = line.split('|')
                ingredient_name = list_line[0].strip()
                quantity = int(list_line[1].strip())
                measure = list_line[2].strip()
                ingredient = {'ingredient_name':ingredient_name, 'quantity':quantity, 'measure':measure}
                list_ingredients.append(ingredient)
        cook_book.setdefault(name_dish, list_ingredients)

def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish in dishes:
        recept = cook_book.get(dish)
        for i in recept:
            dic = {}
            key = i.get('ingredient_name')
            x=0
            if key in res:
                x += (res[key]['quantity'])
            value = {'measure':i['measure'], 'quantity':(i['quantity'])+x}
            dic.setdefault(key,value)
            res.update(dic)
    for i in res.values():
        i['quantity'] *= person_count
    print(res)

get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)