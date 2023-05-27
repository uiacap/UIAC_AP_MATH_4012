import re


def calc_fib(start, end):
    a, b = 0, 1

    while a < start:
        a, b = b, a + b

    lst = []
    while a < end:
        lst.append(a)
        a, b = b, a + b
    return lst


s = input()

first_num, second_num = re.findall(r'\d+', s)
first_num = int(first_num)
second_num = int(second_num)

print(first_num, second_num)

fib_between = []
for i in calc_fib(first_num, second_num):
    if i % 2 == 0:
        fib_between.append(i)

print(fib_between)
