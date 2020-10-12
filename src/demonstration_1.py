"""
You are given a binary tree.
​
Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.
​
Example:
​
Given the binary tree [5,12,32,None,None,8,4],
​
    5
   / \
  12  32
     /  \
    8    4
​
your function should return the depth = 3.
"""
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
​
    def maxDepth(self, root):
        # Your code here
        # base case? 
        # what's the depth of an empty tree? 
        if root is None:
            return 0 
        # how do we get to our base case? 
        # move down the tree all the way until we get to 
        # the node's at the bottom
        # we need the height of left side 
        left_height = self.maxDepth(root.left)
        # we need the height of the right side 
        right_height = self.maxDepth(root.right)
​
        larger_height = max(left_height, right_height)
​
        return 1 + larger_height
​
​
tree = BinaryTreeNode(5)
tree.left = BinaryTreeNode(12)
right = BinaryTreeNode(32)
right.right = BinaryTreeNode(4)
right.left = BinaryTreeNode(8)
tree.right = right
​
print(tree.maxDepth(tree))