

def solution(K, M, A):
    #mainloop just checks every possible minimum sum for a set, starting at the largest number in the starting set
    sizeOfSet = 0
    countOfSets = 0
    arrangementFound = False
    M = max(A)-1
    while (arrangementFound == False):
        M += 1
        arrangementFound = True
        for i in range(len(A)):
            if sizeOfSet + A[i] <= M:
                sizeOfSet += A[i]
            else:
                sizeOfSet = A[i]
                countOfSets += 1
                
            if countOfSets == K:
                countOfSets = 0
                sizeOfSet = 0
                arrangementFound = False
                break

        
    return M