a = int (input("Введите число для определения его статуса "))
x = 0
y = 1
n = 2
while y < a:
    x, y = y, x+y
    n +=1
if y == a:
    print( n)
else :
    print ("-1")
