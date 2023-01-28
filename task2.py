# Задача 2: Найдите сумму цифр трехзначного числа.

num = int(input('Введите трехзначное число: '))
strNum = str(num)
sum = int(strNum[0]) + int(strNum[1]) + int(strNum[2])
sum2 = int((num // 100) + ((num / 10) % 10) + (num % 10))

if abs(num) >= 100 and abs(num) < 1000:
    print(f'{sum} and {sum2}')
else:
    print('Вы ввели не трехзначное число')
