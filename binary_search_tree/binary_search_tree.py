"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if new value is >= the current node value, Go right.
        if value >= self.value:
            # if there is no node there
            if self.right is None:
                # create new node
                self.right = BSTNode(value)
            # (there is a BSTNode to the right), recurse (do the same thing and compare if its less than or greater than)
            else:
                # insert value to self.right
                self.right.insert(value)
        # if new value is < the current node value, Go left.
        if value < self.value:
            # if there is no node to the left
            if self.left is None:
                # Create new node
                self.left = BSTNode(value)
            # (there is a BSTNode to the left), recurse (do the same thing and compare if its less than or greater than)
            else:
                # insert value to self.left
                self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if target is the first node
        if target == self.value:
            return True
        # if target is < the first node go left
        if target < self.value:
            # if there is nothing to the left return None
            if self.left is None:
                return False
            # if there is a value to the left, recurse (check if the target == self.value)
            else:
                return self.left.contains(target)
        # if target is > self.value, go right
        if target > self.value:
            # if there is nothing to the right return False
            if self.right is None:
                return False
            # if there is a node to the right, recurse(check if the target == self.value)
            else:
                return self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        # root of BST
        current_node = self
        # go right until the node doesn't have a right node
        while current_node.right is not None:
            # make the last right node the cur_node
            current_node = current_node.right
        # return the value
        return current_node.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Will have to look at both branches
        # Start at the root
        fn(self.value)
        if self.left is not None:
            # Go left
            self.left.for_each(fn)
        if self.right is not None:
            # Go right
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  
