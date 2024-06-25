#!/usr/bin/env python
# coding: utf-8

# In[35]:


class Treenode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def level(self):
        level =0
        p = self.parent
        while p:
            level=level+1
            p = p.parent
        return level
    def print_tree(self):
        spaces = ' ' * self.level() * 3
        prefix = spaces + "|_ _" if self.parent else ""
        print(prefix + self.data)
        if len(self.children):
            for child in self.children:
                child.print_tree()
            
def build_tree():
    root = Treenode("Electronics")
    
    laptops = Treenode("Laptop")
    laptops.add_child(Treenode("Mac"))
    laptops.add_child(Treenode("surface"))
    laptops.add_child(Treenode("Thinkpad"))
    
    cellphone = Treenode("Cellphone")
    cellphone.add_child(Treenode("iphone"))
    cellphone.add_child(Treenode("googlepixel"))
    cellphone.add_child(Treenode("vivo"))

    tv = Treenode("Tv")
    tv.add_child(Treenode("samsung"))
    tv.add_child(Treenode("LG"))
    
    root.add_child(laptops)
    root.add_child(cellphone)
    root.add_child(tv)
    return root
if __name__ == '__main__':
    root = build_tree()
    root.print_tree()
    pass
        


# In[ ]:




