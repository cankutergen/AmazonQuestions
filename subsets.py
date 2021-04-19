def subsets(arr):
  res = []

  def backtrack(start, temp):
      res.append(temp.copy())

      for i in range(start, len(arr)):
          temp.append(arr[i])
          backtrack(i + 1, temp)
          temp.pop()

  backtrack(0, [])
  res = ""
    
    
 def subsets2(arr):
  res = []

  def backtrack(start, temp):
      res.append(temp.copy())

      for i in range(start, len(arr)):
          if i > start and arr[i] == arr[i-1]:
              continue

          temp.append(arr[i])
          backtrack(i + 1, temp)
          temp.pop()

  backtrack(0, [])
