# Распаковка параметров и параметры функции

# 1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params() # без параметров
print_params(5)  # 1 параметр
print_params(5, 10) # 2 параметра
print_params(5, 10, 15) # 3 параметра

print_params(b = 25)
print_params(c = [1,2,3])

# 2.Распаковка параметров:

values_list = [54.32, 'Строка' , True]
values_dict = {'a': 54.32, 'b': 'Строка', 'c': True }

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)