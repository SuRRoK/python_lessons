#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.
fist_film_coma = my_favorite_movies.find(',')
fist_film = my_favorite_movies[:fist_film_coma]
print(fist_film)

last_film_coma = my_favorite_movies.rfind(',')
last_film = my_favorite_movies[last_film_coma + 2:]
print(last_film)

second_film_coma = my_favorite_movies.find(',', fist_film_coma + 2)
second_film = my_favorite_movies[fist_film_coma + 2:second_film_coma]
print(second_film)

second_from_end_film_coma = my_favorite_movies.rfind(',', 0, last_film_coma - 2)
second_from_end_film = my_favorite_movies[second_from_end_film_coma + 2: last_film_coma]
print(second_from_end_film)
