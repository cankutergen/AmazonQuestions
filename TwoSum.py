def find_sum_of_two(A, val):
    
    dict = {}
    for i in range(len(A)):
        target = val - A[i]

        if target not in dict:
            dict[A[i]] = i
        else:
            return [i, dict[target]]

    return -1
