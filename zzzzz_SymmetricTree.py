  def isSymmetric(root: TreeNode) -> bool:
      if root is None:
          return True
      return check(root.left, root.right)

  def check(self, left, right):
      if left is None or right is None:
          return left == right

      if left.val != right.val:
          return False

      return check(left.left, right.right) and check(left.right, right.left)
