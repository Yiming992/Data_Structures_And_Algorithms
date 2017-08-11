"""
Implement Queue data structure with python list
"""
class Queue():

    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        return self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items==[]

    def size(self):
        return len(self.items)
