  def zeroSum(arr):       
      dict = {}
      sum = 0

      for i in range(len(arr)):
          sum += arr[i]

          if sum == 0:
              return True

          if sum not in dict:
              dict[sum] = i
          else:
              return True

      return False
