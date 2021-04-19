    def lengthOfLIS(nums: List[int]) -> int:
        if not nums:
            return 0
        memo = {}
        return dfs(nums, memo, 0, -sys.maxsize)

    def dfs(nums, memo, i, pre):
        if i == len(nums):
            return 0
        
        if (i, pre) in memo:
            return memo[(i, pre)]
        
        res = dfs(nums, memo, i + 1, pre)
        
        if nums[i] > pre:
            res = max(res, 1 + dfs(nums, memo, i + 1, nums[i]))
        
        memo[(i, pre)] = res
        return res
