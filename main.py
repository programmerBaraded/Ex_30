# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

princ = input("Введите первый элемент, разность и количество элементов: ")
princ = list(princ.split())
princ = list(map(int, princ))

print(princ)
my_list = [princ[0] + i*princ[1] for i in range(princ[2])]
my_list = list(map(str, my_list))
print('\n'.join(my_list))