#!/usr/bin/env python
# coding: utf-8

# In[34]:


from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
def ismatch(ch1, ch2):
    matchdict = {'}' : '{',
               ']' : '[',
               ')' : '('}
    return matchdict[ch1] == ch2
        

def isbalanced(s):
    stack = Stack()
    for ch in s :
        if ch == '{' or ch == '[' or ch == '(':
            stack.push(ch)
        if ch == '}' or ch == ']' or ch ==')':
            if stack.size() == 0 :
                return False
            if not ismatch(ch, stack.pop()):
                return False
    return stack.size() == 0 
if __name__ == '__main__':
    print(isbalanced("}}a+b})") )
    print(is_balanced("({a+b})"))
    print(is_balanced("((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("([a+g])"))
    print(is_balanced(")())"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))


# In[ ]:




