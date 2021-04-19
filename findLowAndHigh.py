def findLowAndHigh(arr, key):
    leftIndex = -1
    rightIndex = -1

    left, right = 0, len(arr) - 1

    # left boundary
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == key:
            leftIndex = mid
            right = mid - 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    left, right = 0, len(arr) - 1

    # right boundary
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == key:
            rightIndex = mid
            left = mid + 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return [leftIndex, rightIndex]
