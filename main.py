#Типы переменных
#Первая задача-созание переменных с одинаковым ид и хначением
name1 = 5
name2 = 5
name3 = 5
print(id(name1))
print(id(name2))
print(id(name3))

#Вторая задача- создание переменных одинакового типа но с разным значением ид
name4 = {"Слава Україні"}
name5 = {"Слава Укрвїні"}
print(id(name4))
print(id(name5))

#Третье задание-замена тип данных
name1 = str(name1)
name2 = float(name2)
name3 = bool(name3)
print(id(name1))
print(id(name2))
print(id(name3))
name4 = name5
print(id(name4))
print(id(name5))


