# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger

ingredients_list = []
coma = ', '

for name, is_added in my_burger.ingredients.items():
    ingredients_list.append(name)
print()
print('Список доступных ингридиентов: ', coma.join(ingredients_list))
print()

my_ingredients = []


def cheeseburger(ingredients):
    my_burger.add_bun(ingredients)
    my_burger.add_cutlet(ingredients)
    my_burger.add_cucumber(ingredients)
    my_burger.add_cheese(ingredients)
    my_burger.add_sauce(ingredients)


cheeseburger(my_burger.ingredients)

for name, is_added in my_burger.ingredients.items():
    if is_added:
        my_ingredients.append(name)

print()
print('Ваш бутерброд состоит из: ', coma.join(my_ingredients))
