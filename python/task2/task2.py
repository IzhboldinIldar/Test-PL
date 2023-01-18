import math

file1 = open(r"C:\python\task2\file1.txt", "r")
radius = file1.read()
r = float(radius)

with open(r"C:\python\task2\file2.txt", "r") as base:

    for line in base.read().splitlines():
        one, two = [[int(j) for j in i.split(' ')] for i in line.split(' ') if i]
        x = float(one[0])
        y = float(two[0])
        sum_count = sum(1 for _ in base)
        
    if sum_count < 100:
        hypotenuse = math.sqrt(x ** 2 + y ** 2)
        if hypotenuse <= r:
            print("Точка c координатами {m1} {m2} принадлежит кругу".format(m1=x, m2=y))
        else:
            print("Точка с координатами {m1} {m2} не принадлежит кругу".format(m1=x, m2=y))
    else:
         pass