import findMinMax, Sumrange
import random                   # 파이썬 제공 내장 모듈

A = []
for _ in range(10):
    A.append(random.randint(1,100))

print("(min, max) = ", findMinMax.find_min_max(A))
print("Sum =", Sumrange.sum_range(1, 10))