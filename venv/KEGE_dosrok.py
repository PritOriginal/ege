def calc(x,a,b):
	x = int(str(x),a)
	s = ""
	while x > 0:
		s += str(x % b)
		x //= b
	return s[::-1]

# № 5
# for N in range(1,100):
# 	k = calc(N,10,2)
# 	if N % 2 == 0:
# 		k = k + "10"
# 	else:
# 		k = "1" + k + "01"
# 	k = calc(k,2,10)
# 	if int(k) > 516:
# 		print(N)

# № 6
# for i in range(1, 100):
# 	s = i
# 	s = (s - 10) // 7
# 	n = 1
# 	while s > 0:
# 		n = n*2
# 		s = s - n
# 	if n == 8:
# 		print(i)
# 		break

# № 12
# s = ""
# for i in range(86):
# 	s += "8"
# while s.find("1111") != -1 or s.find("8888") != -1:
# 	if s.find("1111") != -1:
# 		s = s.replace("1111","8",1)
# 	else:
# 		s = s.replace("8888","11",1)
# print(s)

# № 14
# x = calc(3*16**2018 - 2*8**1028 - 3*4**1100 - 2**1050 - 2022, 10, 4)
# print(x.count("3"))

# № 15
# def d(n,m):
# 	if n % m == 0:
# 		return 1
# 	else:
# 		return 0
#
# def d_(n,m):
# 	if n % m != 0:
# 		return 1
# 	else:
# 		return 0
#
# for A in range(1,999):
# 	k = 1
# 	for x in range(1,999):
# 		if ( (d(x,3) <= d_(x,5)) or (x + A >= 70) ) == 0:
# 			k = 0
# 			break
# 	if k == 1:
# 		print(A)

# №16
# def f(n):
# 	if n < 3:
# 		return 2
# 	elif n > 2 and n % 2 == 0:
# 		return f(n-1) + f(n-2) - n
# 	elif n > 2 and n % 2 != 0:
# 		return f(n-2) - f(n-1) + 2*n
#
# print(f(30))

# №17
# f = open("C:/Users/Stepan/Downloads/17(2).txt")
# num = list(f)
# min_ = 0
# for n in num:
# 	if int(n) % 17 == 0:
# 		if min_ == 0 or min_ > int(n):
# 			min_ = int(n)
# i = 0
# k = 0
# max_ = 0
# while i < len(num) - 1:
# 	if int(num[i]) % min_ == 0 or int(num[i+1]) % min_ == 0:
# 		k += 1
# 		if int(num[i]) + int(num[i+1]) > max_:
# 			max_ = int(num[i]) + int(num[i+1])
# 	i += 1
# print(k, max_)

# № 19-21
# def f1(x,y,p):
# 	if x+y >= 223 or p > 3:
# 		return p == 3
# 	return f1(x+1,y,p+1) or f1(x,y+1,p+1) or f1(x*2,y,p+1) or f1(x,y*2,p+1)
#
# def f2(x,y,p):
# 	if x+y >= 223 or p > 4:
# 		return p == 4
# 	if p % 2 != 0:
# 		return f2(x+1,y,p+1) or f2(x,y+1,p+1) or f2(x*2,y,p+1) or f2(x,y*2,p+1)
# 	else:
# 		return f2(x + 1, y, p + 1) and f2(x, y + 1, p + 1) and f2(x * 2, y, p + 1) and f2(x, y * 2, p + 1)
#
# def f3(x,y,p): # №21
#     if x+y >= 223 or p > 5:
#         return p == 3 or p == 5
#     if p%2 == 0:
#         return f3(x+1,y,p+1) or f3(x,y+1,p+1) or f3(x*2,y,p+1) or f3(x,y*2,p+1)
#     else:
#         return f3(x+1,y,p+1) and f3(x,y+1,p+1) and f3(x*2,y,p+1) and f3(x,y*2,p+1)
#
# for s in range(1, 205 + 1):
# 	if f2(17,s,1):
# 		print(s)

# № 22
# def f(i):
# 	s = i
# 	P = 10
# 	Q = 8
# 	K1 = 0
# 	K2 = 0
# 	while s <= 100:
# 		s = s + P
# 		K1 = K1 + 1
#
# 	while s >= Q:
# 		s = s - Q
# 		K2 = K2 + 1
# 	K1 += s
# 	K2 += s
# 	return K1,K2
#
# for i in range(1, 1000):
# 	if f(i) == (10,19):
# 		print(i)
# 		break

# №24
# f = open("C:/Users/Stepan/Downloads/24(1).txt")
# st = f.read()
# m = 0
# s_m = ""
# s_ = ""
# k = 0
# b = 0
# for s in st:
# 	if s == "A" and b == 0:
# 		b = 1
# 		s_ += s
# 	elif (s == "B" or s == "C") and b == 1:
# 		k += 1
# 		s_ += s
# 		b = 0
# 	else:
# 		b = 0
# 		if k > m:
# 			m = k
# 			s_m = s_
# 		k = 0
# 		s_ = ""
# print(m,s_m)
#
# № 25
# for i in range(100000000,10**9):
# 	s = str(i)
# 	if s[0:5:] == "12345" and s[6] == "6" and s[8] == "8":
# 		if i % 17 == 0:
# 			print(i,i/17)
