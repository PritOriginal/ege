# Перевод числа x из a-ричной системы счисления в b-ричную
def calc(x,a,b):
    x = int(str(x), a)
    s = ''
    while x > 0:
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

s = calc(3*4**38+2*4*23+4**20+3*4**5+2*4**4+1, 10, 16)
k=0
for j in s:
    if (j == "0"):
        k += 1
print(k)