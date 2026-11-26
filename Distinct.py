def solution(A):
    if len(A) == 0:
        return 0
    A.sort()
    pointerNow = -1
    distinctValues = 0
    for i in range(len(A)):
        if not pointerNow == A[i]:
            distinctValues += 1
        pointerNow = A[i]
    return distinctValues

