class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = []

        if root:
            q.append(root)

        while not q.empty():
            level = []

            for _ in range(q.qsize()):             
                node = q.pop(0)
                level.append(node.val)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            arr.append(level)

        return arr
