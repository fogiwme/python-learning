import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(10, 'cucumbers', 'tomatos', 'cheese')

# ИЛИ

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(10, 'cucumbers', 'tomatos', 'cheese')

# ИЛИ

from pizza import * 
"""Импортирует все функции из модуля pizza.py"""

make_pizza(10, 'pepperoni')

# ИЛИ 

import pizza as p

p.make_pizza(13, 'cucumbers')