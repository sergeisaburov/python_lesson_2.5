#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print('задача № 1. Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.')
for i in range(1,6):
    print(i ,  0 )
print('задача № 1 - Конец ')


print('задача № 2 Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.')
t1=0
for i in range(1,11):
    print("Введите", i, "число")
    chislo = int(input())
    print("Введено", i, "число")
    while chislo > 0:
        if chislo % 10 == 5:
         t1 = t1+1
        chislo = chislo // 10
    print("Всего введено", t1, 'пятерок')
print("всего пятерок", t1)
print('задача № 2 - Конец')

print('задача № 3 Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.')
sum=0
for i in range(1,101):
    sum += i
    print( i,'общая сумма в этой строке:', sum - i, '+', i , '=', sum )
print('задача № 3 - ОТВЕТ = ', sum)
print('задача № 3 - Конец')

print('задача № 4 Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.')
proizvedenie=1
for i in range(1,10):
    proizvedenie *= i
    print( i,'произведение в этой строке:',  proizvedenie, '*',i+1, '=', proizvedenie*(i+1) )
print('задача № 4 - ОТВЕТ = ', proizvedenie)
print('задача № 4 - Конец')

print('задача № 5 Вывести цифры числа на каждой строчке. Введите число:')
chislo = int(input())
while chislo>0 :
    print(chislo%10)
    chislo=chislo//10
print('задача № 5 - Конец')

print('задача № 6 Найти сумму цифр числа. Введите число:')
chislo = int(input())
t=0
while chislo>0 :
    if chislo%10 > 0:
        t = chislo%10+t
    chislo=chislo//10
print("Сумма=", t)
print('задача № 6 - Конец')

print('задача № 7 Найти произведение цифр числа. Введите число:')
chislo = int(input())
t=1
while chislo>0 :
    if chislo%10 > 0:
        t = chislo%10*t
    chislo=chislo//10
print("Произведение=", t)
print('задача № 7 - Конец')

print('задача № 8 Дать ответ на вопрос: есть ли среди цифр числа 5. Введите число:')
chislo = int(input())
while chislo>0 :
    if chislo%10 ==5:
       print('Да, есть')
       break
    chislo=chislo//10
else: print("Нет, нету")
print('задача № 8 - Конец')

print('задача № 9 Найти максимальную цифру в числе. Введите число:')
chislo = int(input())
poisk_chisla = chislo%10
chislo=chislo//10
while chislo>0 :
    if chislo%10 > poisk_chisla:
        print("Дошел", poisk_chisla )
        poisk_chisla = chislo % 10
    chislo = chislo // 10
print("Максимальная цифра в числе:", poisk_chisla )
print('задача № 9 - Конец')

print('задача № 10 Найти количество цифр 5 в числе')
chislo = int(input())
chislo = chislo%10
chislo=chislo//10
while chislo>0 :
    if chislo%10 > poisk_chisla:
        print("Дошел", poisk_chisla )
        poisk_chisla = chislo % 10
    chislo = chislo // 10
print("Максимальная цифра в числе:", poisk_chisla )
print('задача № 10 - Конец')
