def permutation(arr):
    res = []
    visited = set()

    def backtrack(temp):
        if len(temp) == len(arr):
            res.append(temp.copy())
            return

        for i in range(len(arr)):
            if i not in visited:
                visited.add(i)
                temp.append(arr[i])

                backtrack(temp)

                visited.remove(i)
                temp.pop()

    backtrack([])
    return res
