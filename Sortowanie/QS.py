from timeit import default_timer as timer
from datetime import timedelta


#QuickSort
def quick_sort(A, p, r):
    start_time = timer()
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)
        end_time = timer()
        print(timedelta(seconds=end_time - start_time))


def partition(A, p, r):
    pivot = A[r]
    smaller = p
    for j in range(p, r):
        if A[j] <= pivot:
            A[smaller], A[j] = A[j], A[smaller]
            smaller = smaller + 1
    A[smaller], A[r] = A[r], A[smaller]
    return smaller


A = [5, 2, 1, 11, 15, 13, 16, 4, 2, 0, 2, 12, 9, 4, 3, 6, 9, 12, 11, 18, 17]

quick_sort(A, 0, len(A) - 1)

print(A)


