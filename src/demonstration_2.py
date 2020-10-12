"""
You are given a binary tree. You need to write a function that can determine if
it is a valid binary search tree.
​
The rules for a valid binary search tree are:
​
- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- Both the left and right subtrees must also be valid binary search trees.
​
Example 1:
​
    5
   / \
  3   7
​
Input: [5,3,7]
Output: True
​
Example 2:
​
    10
   / \
  2   8
     / \
    6  12
​
Input: [10,2,8,None,None,6,12]
Output: False
Explanation: The root node's value is 10 but its right child's value is 8.
​
Example 2:
​
    10
   / \
  2   11
     / \
    6  12
​
Input: [10,2,11,None,None,6,12]
Output: False
Explanation: The root node's value is 10 but it has a child in the right sub-tree
that is less than it.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
​
    def check(self, upper, lower):
        # base case?
        # 1. return False when the value of self is not in the upper and lower bound 
        if self.value < lower or self.value > upper:
            return False
        # 2. return True when we've traversed all the way down the tree with no issues
        if not self.left and not self.right:
            return True 
        # how do we get closer to our base case? 
        # traverse down the tree by checking the children nodes 
        return self.left.check(self.value - 1, lower) and self.right.check(upper, self.value + 1)
​
    def is_valid_BST(self):
        # Your code here
        # Idea 1:    
        # keep track of the min possible value and max possible value for a node 
        # when we traverse left, update the max possible value 
        # when we traverse right, update the min possible value 
        # check if the current node's value falls within the given range 
        return self.check(float("inf"), float("-inf"))
​
        # Idea 2:
        # get all of the elements out of the binary tree in order 
        # (a valid binary search tree would give back all its elements in sorted order)
        # check if order of the elements from the tree matches the order of the same 
        # elements in sorted order 
​
tree = TreeNode(10)
tree.left = TreeNode(2)
right = TreeNode(11)
right.left = TreeNode(6)
right.right = TreeNode(12)
tree.right = right
​
print(tree.is_valid_BST())