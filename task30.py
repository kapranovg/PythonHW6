# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a, d, n = (int(input()) for _ in 'adn')
res = []


while n > 0:
    c = a + (n-1) * d
    n -= 1
    res.append(c)

res.reverse()
print(res)      
