import random

A = []


def randInts(A):
    for i in range(100000):
        rand = random.randint(0, 1000)
        A.append(rand)


randInts(A)
