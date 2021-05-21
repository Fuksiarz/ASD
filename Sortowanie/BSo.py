from timeit import default_timer as timer
from datetime import timedelta





# BubbleSort odwrotne
def sortowanie_babelkowe(lista):
    start = timer()

    n = len(lista)

    while n > 1:
        zamien = False
        for l in range(0, n - 1):
            if lista[l] < lista[l + 1]:
                lista[l], lista[l + 1] = lista[l + 1], lista[l]
                zamien = True

        n -= 1
        end = timer()
        print(timedelta(seconds=end - start))
        if zamien == False: break


array = [5, 2, 1, 11, 15, 13, 16, 4, 2, 0, 2, 12, 9, 4, 3, 6, 9, 12, 11, 18, 17]

sortowanie_babelkowe(array)
print(array)
