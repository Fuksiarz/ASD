A = [1, 3, 5, 7, 8, 9, 11, 22]
B = [1, 2, 2, 3, 5, 8, 6, 6, 9, 22]
D = "cokolwiek"


def glowa(A):
    if len(A) > 0:
        return A[0]


def ogon(A):
    if len(A) > 0:
        A.pop(0)
    return A


def jestPusta(A):
    if (len(A) > 0):
        return True
    else:
        return False


licz = 0


def czescWspolna(A, B):
    if jestPusta(A) & jestPusta(B):

        if glowa(A) == glowa(B):

            print(glowa(A))

            ogon(B)
            ogon(A)

            return czescWspolna(A, B)
        elif glowa(A) > glowa(B):
            ogon(B)

        else:
            ogon(A)
        return czescWspolna(A, B)
    exit()

def reverse(A):
    if(jestPusta(A)):

        if len(A) <= 1:
            return A
        else:
            return A[len(A) - 1] + reverse(A[:len(A) - 1])
    else:
        exit()



print(reverse(D))

czescWspolna(A, B)




