# Мои решения некоторых задач в варианте [Открытый пробник 01.2022] на КЕГЭ

# def calc(x,a,b):
#     x = int(str(x), a)
#     s = ''
#     while x > 0:
#         if (x % b) > 10:   # Модификация для проверки буквенных чисел
#             s += 'a'       #
#         else:
#             s += str(x % b)
#         x //= b
#     return s[::-1]

# № 24
# f = open("C:/Users/Stepan/Desktop/24(1).txt")
# k = 0
# for line in f:
#     i = 0
#     while i < len(line)-3:
#         if line[i] == "Z":
#             if line[i+2] == "R" and line[i+3] == "O":
#                 k += 1
#                 break
#         i += 1
# print(k)

# № 25
# for i in range(164700, 164752):
#     k = 0
#     max = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             k += 1
#             if j != i:
#                 max = j
#     if k == 6:
#         print(max,i)

# № 5
# for N in range(999):
#     X = N
#     N = str(calc(N,10,2))
#     n1 = N.count("1")
#     n0 = N.count("0")
#     if n1 > n0:
#         N = N + "0"
#     else:
#         N = "11" + N
#     n1 = N.count("1")
#     n0 = N.count("0")
#     if n1 > n0:
#         N = N + "0"
#     else:
#         N = "11" + N
#     #print(N)
#     if int(calc(int(N), 2, 10)) > 500:
#         print(X)

# № 26
# f = open("C:/Users/Stepan/Downloads/26.txt")
# N = 9999
# K = 978
# s = list()
# i = 0
# for line in f:
#     if i == 1:
#         s.append(int(line))
#     else:
#         i = 1
# s = sorted(s,reverse=True)
# A = list()
# i = 0
# while i < K:
#     A.append(s[i])
#     i += 1
# sum = 0
# for h in A:
#     sum += h
# print(sum)