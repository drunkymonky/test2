import re

pattern = re.compile('^world$') # создание шаблона регулярного выражения.
# ^ с начала текста строго
# $ с конца текста
value = 'world, hello something'
print(re.search(pattern, value))

pattern = re.compile('\w\w\w') # состоит из трех букв это замена символа a-z A-Z и 0-9
pattern = re.compile('\d') # одно цисло
pattern = re.compile('\s') # все непечатные символы, таб, пробел и \n

pattern re.compile('^\d{4}$') # строка сотоящая из 4 цифр
pattern re.compile('^\d{4,10}$') # строка сотоящая от 4 до 10 чисел
pattern re.compile('^\d{4,}$') # строка сотоящая от 4 цифр и до бесконечности
pattern re.compile('^\d{,}$') # строка сотоящая из цифр
pattern re.compile('(.*)') # строка сотоящая из цифр
print(re.search(pattern, 'dsf3424') is not None)

# 1
pattern = re.compile('^\d\d\w\d\d\w\d{4}$')

# 2
pattern = re.compile('\+7-?\d{3}-?\d{3}-?\d{2}-?\d{2}')

# 3
pattern = re.compile('[24680]$')

# 4
pattern = re.compile('')
















































































































































































































print(re.search(pattern, 'abF'))







