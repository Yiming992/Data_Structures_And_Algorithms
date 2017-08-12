
"""
Simulate Hot-Potato problem
"""
from Queue import Queue

def hot_potato(Names,count):
    queue=Queue()

    for i in Names:
        queue.enqueue(i)
    counter=0
    while queue.size()>1:
        if counter%count==0 and counter>0:
            queue.dequeue()
        pop=queue.dequeue()
        queue.enqueue(pop)
        counter+=1
    return queue.dequeue()

print(hot_potato(['Bill','David','Susan','Jane','Kent','Brad'],7))
