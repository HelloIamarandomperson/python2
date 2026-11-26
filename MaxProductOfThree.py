def solution(A):
    High1 = -1001
    High2 = -1001
    High3 = -1001
    Neg1 = 0
    Neg2 = 0
    for i in range(len(A)):
        if High1 < A[i]:
            High3 = High2
            High2 = High1
            High1 = A[i]
        elif High2 < A[i]:
            High3 = High2
            High2 = A[i]
        elif High3 < A[i]:
            High3 = A[i]
        if Neg1 > A[i]:
            Neg2 = Neg1
            Neg1 = A[i]
        elif Neg2 > A[i]:
            Neg2 = A[i]
    if (Neg1*Neg2) > (High3*High2):
        return Neg1*Neg2*High1
    return High1*High2*High3

