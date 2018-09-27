class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.size=k
        self.items=[]
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.items)==self.size:
            return False
        self.items.insert(0,value)
        return True
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.items)==self.size:
            return False
        self.items.append(value)
        return True
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if len(self.items)==0:
            return False
        self.items.pop(0)
        return True
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if len(self.items)==0:
            return False
        self.items.pop()
        return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if len(self.items)==0:
            return -1
        return self.items[0]
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if len(self.items)==0:
            return -1
        return self.items[-1]
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if len(self.items)==0:
            return True
        else:
            return False
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if len(self.items)==self.size:
            return True
        else:
            return False