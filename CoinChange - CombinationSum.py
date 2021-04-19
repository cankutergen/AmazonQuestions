def solve_coin_change(denominations, amount):

    res = []

    def backtrack(start, target, temp):
        if target == 0:
            res.append(temp.copy())
            return

        if target < 0:
            return

        for i in range(start, len(denominations)):
            temp.append(denominations[i])

            backtrack(i, target - denominations[i], temp)

            temp.pop()

    backtrack(0, amount, [])
    
    if len(res) == 0:
        return -1
    else:
        return len(res)
