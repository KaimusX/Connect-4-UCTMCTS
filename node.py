class TreeNode:
    def __init__(self, parent=None):
        self.wi = 0
        self.ni = 0
        self.children = {}  # col (1-indexed) -> TreeNode
        self.parent = parent
