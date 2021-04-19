  def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      if not root: 
          return None

      p_path = pathToNode(root, p, [])
      q_path = self.pathToNode(root, q, [])

      if len(p_path) <= len(q_path):
          longer = q_path
          shorter = p_path
      else:
          longer = p_path
          shorter = q_path

      matching = [x for x in longer if x in shorter]
      return matching[-1]

  def pathToNode(node, x, path):
      if node is None:
          return []

      if node.val == x.val:
          path.append(x)
          return path

      left = pathToNode(node.left, x, path + [node])
      right = pathToNode(node.right, x, path + [node])

      if left: return left
      if right: return right
      
      
      
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

      # both of them in the left subtree
      if p.val < root.val and q.val < root.val:
          return self.lowestCommonAncestor(root.left, p, q)
      # both in them in the right subtree
      elif p.val > root.val and q.val > root.val:
          return self.lowestCommonAncestor(root.right, p, q)
      # one is on the right and other is the left 
      # so the answer is the root
      else:
          return root
