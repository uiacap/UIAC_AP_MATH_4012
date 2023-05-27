import math
import random


def quadratic(a, b, c):
    d = b ** 2 - 4 * a * c

    if d < 0:
        return None, None
    elif d == 0:
        return -b / (2 * a), None
    else:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        if root1 < root2:
            root1, root2 = root2, root1
        return root1, root2


s1 = int(input())
s2 = int(input())
s3 = int(input())

random.seed(s1)
a = random.randint(-100, 100)
random.seed(s2)
b = random.randint(-100, 100)
random.seed(s3)
c = random.randint(-100, 100)

r1, r2 = quadratic(a, b, c)
print(r1, r2)
