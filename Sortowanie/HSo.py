from timeit import default_timer as timer
from datetime import timedelta



# HeapSort odwrotnie
def Heapify(arr, n, i):
    najwieksza = i
    lewo = 2 * i + 1
    prawo = 2 * i + 2
    if lewo < n and arr[i] > arr[lewo]:
        najwieksza = lewo
    if prawo < n and arr[najwieksza] > arr[prawo]:
        najwieksza = prawo
    if najwieksza != i:
        arr[i], arr[najwieksza] = arr[najwieksza], arr[i]
        Heapify(arr, n, najwieksza)


def Heap_Sort(arr):
    start = timer()
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        Heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)
        end = timer()
        print(timedelta(seconds=end - start))


arr = [5, 2, 1, 11, 15, 13, 16, 4, 2, 0, 2, 12, 9, 4, 3, 6, 9, 12, 11, 18, 17]
Heap_Sort(arr)
print(arr)



