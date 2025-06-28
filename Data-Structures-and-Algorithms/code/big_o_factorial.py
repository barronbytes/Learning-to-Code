# O(n!) — Factorial time


def num_possibilities(num):
    total = 1
    for x in range(1, num+1):
        total *= x
    return total


num = 5
result = num_possibilities(num)
print("Total possibilities:", result)


"""
Here are other example(s):


def num_possibilities(num):
    total = 1
    if num > 1:
        total = num * num_possibilities(num - 1)
    return total


def num_possibilities(num):
    total = num * num_possibilities(num - 1) if num > 1 else 1
    return total

"""