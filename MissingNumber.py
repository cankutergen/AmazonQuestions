  def missingNumber(nums: List[int]) -> int:

      n = len(nums) + 1
      set_nums = set(nums)

      for i in range(1, n + 1):
          if i not in set_nums:
              return i

      return -1
