import math
n = int(input())
k = int(input())
def apples(n, k):
    return math.floor(k/n)
print(apples(n, k))