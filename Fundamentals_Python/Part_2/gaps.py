print("Python")

print("\tPython") #"\t" добавляет пробел (таб)#

print("\n") #"\n" приказывает начать текст с новой строки
print("Languages:\nPython\nC\nJavaScript\nHTML")

print("\nLanguages:\n\tPython\n\tC\n\tJavaScript") #\n\t приказывает начать текст с новой строки, в начале которой располагается табуляция#
print('\n')


favorite_language = ' english '
favorite_language_r = favorite_language.rstrip() #"rstrip()" удаляет лишние пробелы у правого края
favorite_language_l = favorite_language.lstrip() #"lstrip()" удаляет лишние пробелы у левого края
favorite_language_r_l = favorite_language.strip() #"strip()" удаляет лишние пробелы у левого и правого края

print(favorite_language)
print(favorite_language_r)
print(favorite_language_l)
print(favorite_language_r_l)
