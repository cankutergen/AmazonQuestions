def reverseWithSize(arr, k):  
    i = 0
    while i <= len(arr) - k:
        left = i
        right = i + k - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        i += k

    return arr
