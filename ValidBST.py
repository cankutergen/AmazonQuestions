def isValid(root):

    def checkNode(root, minimum, maximum):
        
        if root is None:
            return True

        if minimum and root.val <= minimum:
            return False

        if maximum and root.val >= higher:
            return False

        return checkNode(root.left, minimum, root.val) and checkNode(root.right, root.val, maximum)

    return checkNode(root, None, None)
