
def solution(A):
    #the function finds absDistinct in 2 parts, the first sectin will find every normal disinct number in the sequince, the second part will find all of the absolute distinct numbers, so part 1 catches all things 1,1, while part 2 catches all things -1.1
    if len(A) < 2:
            #base case, if the number is 1 or 0, then there will be 1 or 0 distinct numbers
        return len(A)
    Pivot = 0
    PivotValue = A[0]
    current = None
    B = []
    for i in range(len(A)):
        #cycles through the full sorted list and check if each value in the list is the same as the one behind it, if it isn't, it adds it to B
        if current == None or not current == A[i]:
            current = A[i]
            B.append(A[i])
            if A[i] < abs(PivotValue):
                #this is a step needed for part 2, here we want to find the value closest to zero, also known as the pivot, this is useful because the sorted list switches from positive and negative at that point
                PivotValue = A[i]
                Pivot = len(B)-1

    Left = Pivot
    Right = Pivot + 1
    while(True):
        #this will slowly move Right and Left futher apart until one of them reaches the edge, moving whichever one is smaller, and removing the Right one whenever they are the same, since they start at the closest positive and negative, that will mean it will cycle through every non distinct value
        if Left == -1 or Right == len(B):
            return len(B)
        if abs(B[Left]) < B[Right]:
            Left -= 1
        elif abs(B[Left]) > B[Right]:
            Right += 1
        else:
            B.pop(Right)