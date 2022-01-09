'''
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= y) and (y <= w) or (z == (x or y))) == 0):
                    print(x,y,z,w)
'''
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x and y) or (y == z) or w)== 0):
                    print(x,y,z,w)