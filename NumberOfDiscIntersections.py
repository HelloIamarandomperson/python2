
def solution(A):
    Count = 0
    High = None
    while (len(A) > 0):
        High = A[0]
        Count -=1
        for i in range(len(A)):
            if High >= i-A[i]:
                Count += 1
                if Count >= 10000000:
                    return -1
        A.pop(0)
    return Count

