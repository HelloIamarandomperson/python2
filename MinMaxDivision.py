

def solution(K, M, A):
    
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