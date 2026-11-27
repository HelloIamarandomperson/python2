def solution(A):
    #function will find all values in a unsorted list that are distinct by sorting the list then checking each value's neighbors
    if len(A) == 0:
        #base case, if list is empty then there are 0 distinct values
        return 0
    A.sort()
    pointerNow = -1
    distinctValues = 0
    for i in range(len(A)):
        #checks every value to the last one, if they are not the same, distinctValues goes up
        if not pointerNow == A[i]:
            distinctValues += 1
        pointerNow = A[i]
    return distinctValues

