# Перевод числа x из a-ричной системы счисления в b-ричную
def calc(x,a,b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        if (x % b) > 10:   # Модификация для проверки буквенных чисел
            s += 'a'       #
        else:
            s += str(x % b)
        x //= b
    return s[::-1]

#print(calc(123, 10, 2))
'''
s = calc(4**2020 + 2**2017 - 15, 10, 2)
k = 0
for j in s :
    if j == '1':
        k += 1
print(k)
'''

# Решите уравнение: 121x + 110 = 1017
#
# Ответ запишите в троичной системе (основание системы счисления в ответе писать не нужно).

# s = int(calc(101, 7, 10))-1
# x = 3
# while (int(calc(121, x, 10)) != s):
#     x += 1
# print(calc(x, 10, 3))



# Чему равно наименьшее основание позиционной системы счисления x, при котором 225x = 405y?
#
# Ответ записать в виде целого числа.
# x = 2
# while x < 36:
#     y = 2
#     while y < 36:
#         try:
#             if (int(calc(225, x, 10)) == int(calc(405, y, 10))):
#                 print(x)
#         except:
#             print('-')
#         y += 1
#     x += 1


# В системе счисления с основанием N запись числа 8710 оканчивается на 2 и содержит не более двух цифр.
# Перечислите через запятую в порядке возрастания все подходящие значения N.
# x = 1000
# while x > 0:
#     s = calc(87,10,x)
#     if s[-1] == '2' and len(s) < 3:
#         print(x)
#     x -= 1


# Запись числа 338 в системе счисления с основанием N содержит 3 цифры и оканчивается на 2.
# Чему равно максимально возможное основание системы счисления?
#
# Примечание * : Необходима модификация калькулятора, для избежания "буквенных чисел"
#
# n = 1000
# while n > 0:
#     s = calc(338, 10, n)
#     if s[-1] == '2' and len(s) == 3:
#         print(n, s)
#     n -= 1

# Укажите наименьшее основание системы счисления, в которой запись числа 50 трехзначна.
# x = 2
# while x < 1000 :
#     s = calc(50, 10, x)
#     if len(s) == 3:
#         print(x)
#         break
#     x += 1