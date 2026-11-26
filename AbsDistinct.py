
def solution(A):
    if len(A) < 2:
        return len(A)
    Pivot = 0
    PivotValue = A[0]
    current = None
    B = []
    for i in range(len(A)):
        if current == None or not current == A[i]:
            current = A[i]
            B.append(A[i])
            if A[i] < abs(PivotValue):
                PivotValue = A[i]
                Pivot = len(B)-1

    Left = Pivot
    Right = Pivot + 1
    while(True):
        if Left == -1 or Right == len(B):
            return len(B)
        if abs(B[Left]) < B[Right]:
            Left -= 1
        elif abs(B[Left]) > B[Right]:
            Right += 1
        else:
            B.pop(Right)