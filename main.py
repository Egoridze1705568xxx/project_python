from decimal import ROUND_CEILING
import math

n = int(input("Введите число для вычисления факториала: "))
count = 1
i = 0
while i!=n:
    i +=1
    count *= i
print(count)
