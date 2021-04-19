def isValid(root):

    def checkNode(root, lower, higher):
        
        if root is None:
            return True

        if lower and root.val <= lower:
            return False

        if higher and root.val >= higher:
            return False

        return checkNode(root.left, lower, root.val) and checkNode(root.right, root.val, higher)

    return checkNode(root, None, None)
