alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points']) будет ошибка, потому что заданного значения в ключе нет

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#.get() говорит «Дай мне значение по этому ключу. А если ключа нет — не падай с ошибкой»
#словарь.get(ключ, значение_если_ключа_нет)
