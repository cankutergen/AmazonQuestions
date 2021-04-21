class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        curr = []
        
        def backtrack(k, index):
            if k == 0:
                res.append(curr.copy())
                return
            
            for i in range(index, n + 1):
                curr.append(i)
                
                backtrack(k - 1, i + 1)
                
                curr.pop()

        backtrack(k, 1)
        return res
