#!/usr/bin/env python
# coding: utf-8

# In[39]:


class Treenode:
    def __init__(self, name,  desig):
        self.name = name
        self.desig=desig
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
    def print_tree(self, detail):
        if detail == 'both':
            val = self.name + " (" + self.desig + ")"
        elif detail == 'name':
            val = self.name
        else:
            val = self.desig
            
        spaces = ' ' * self.level() * 3
        prefix = spaces + "|_ _" if self.parent else ""
        print(prefix + val)
        if len(self.children):
            for child in self.children:
                child.print_tree(detail)
            
def build_tree():
    
    root = Treenode("Nilupul","CEO")
    
    cto = Treenode("Chinmay","CTO")
    
    ifh = Treenode("Vishwa","Infrastructure head")
    ifh.add_child(Treenode("Dhaval","cloud manager"))
    ifh.add_child(Treenode("Abijith","Appmanager"))
    
    ap = Treenode("Amir","Application Head")
    
    hr = Treenode("Gels","HR head")
    hr.add_child(Treenode("peter","Recruitment Manager"))
    hr.add_child(Treenode("waqas","Policy Manager"))
    
    
    root.add_child(cto)
    cto.add_child(ifh)
    cto.add_child(ap)
    root.add_child(hr)
    return root
if __name__ == '__main__':
    root = build_tree()
    root.print_tree("both")
    root.print_tree("name")
    root.print_tree("desig")

    pass
        


# In[ ]:





# In[ ]:




