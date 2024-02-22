def diagonalDifference(arr):
    d1 = 0
    d2 = 0

    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if(i == j):
                d1 += arr[i][j]
            if(i == len(arr) - j -1):
                d2 += arr[i][j]
    sum = d1-d2
    if(sum > 0 ):
        return sum
    else:
        return sum * -1
