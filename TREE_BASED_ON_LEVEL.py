#!/usr/bin/env python
# coding: utf-8

# In[37]:


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
    def print_tree(self, level):
        if self.level()>level:
            return 
        spaces = ' ' * self.level() * 3
        prefix = spaces + "|_ _" if self.parent else ""
        print(prefix + self.data)
        if len(self.children):
            for child in self.children:
                child.print_tree(level)
                    
def build_tree():
    root = Treenode("Global")
    
    india = Treenode("India")
    gujarat=Treenode("Gujarat")
    gujarat.add_child(Treenode("ahmedabad"))
    gujarat.add_child(Treenode("Baroda"))
    
    karna = Treenode("Karnataka")
    karna.add_child(Treenode("Mysore"))
    karna.add_child(Treenode("Bangalore"))
    
    usa = Treenode("USA")
    newjersey = Treenode("New Jersey")
    newjersey.add_child(Treenode("Princeton"))
    newjersey.add_child(Treenode("Trenton"))
    cali = Treenode("California")
    cali.add_child(Treenode("San Francisco"))
    cali.add_child(Treenode("Mountain View"))
    cali.add_child(Treenode("Palo Alto"))
    root.add_child(india)
    root.add_child(usa)
    india.add_child(gujarat)
    india.add_child(karna)
    usa.add_child(newjersey)
    usa.add_child(cali)
    
    return root
if __name__ == '__main__':
    rootnode = build_tree()
    rootnode.print_tree(2)
    pass
        


# In[ ]:





# In[ ]:




