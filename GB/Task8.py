
# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с
# координатами Х и У
x=4
y=1
if x<0 and y>0:
    print(1)
elif x > 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:
    print("принадлежит координатной оси")