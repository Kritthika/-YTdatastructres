#!/usr/bin/env python
# coding: utf-8

# In[71]:


class Binary_tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binary_tree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binary_tree(data)
    def in_order(self):
        elements = []
        if self.left:
            elements += self.left.in_order()
            
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order()
            
        return elements
    
    def post_order(self):
        elements=[]
        if self.left:
            elements += self.left.post_order()
            
        if self.right:
            elements += self.right.post_order()
            
        elements.append(self.data)
        return elements
    
    def pre_order(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order()
            
        if self.right:
            elements += self.right.pre_order()

        return elements
    
    def search(self, val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def findmin(self):
        if self.left is None:
            return self.data
        return self.left.findmin()
    
    def findmax(self):
        if self.right is None:
            return self.data
        return self.right.findmax()       
            
    def cal_sum(self):
        leftsum = self.left.cal_sum() if self.left else 0
        rightsum = self.right.cal_sum()  if self.right else 0
        return leftsum+rightsum+self.data
                
            
def build_tree(elements):
    root = Binary_tree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root
if __name__ == '__main__':
    numbers = [15, 14, 12, 20, 23, 88, 27, 7]
    numbertree = build_tree(numbers)
    print("inorder:",numbertree.in_order())
    print("preorder:",numbertree.pre_order())
    print("postorder:",numbertree.post_order())
    
    print(numbertree.search(20))
    print("minimum",numbertree.findmin())
    print("maximum",numbertree.findmax())
    print("sum",numbertree.cal_sum())


# In[ ]:





# In[ ]:




