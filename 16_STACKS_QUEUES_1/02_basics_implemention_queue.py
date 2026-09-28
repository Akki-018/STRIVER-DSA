## QUEUE ARE ALSO LIKE STACKS - BUT THEY FOLLOW FIFO PRINCIPLE i.e First in first out
# IMPLEMENTATION OF QUEUE USING ARRAYS
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,x):
        self.queue.append(x)
    def dequeue(self):
        return self.queue.pop(0)
    def front(self):
        return self.queue[0]
    def isEmpty(self):
        return len(self.queue)==0
    def display(self):
        return self.queue
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.display())
print(q.front())
print(q.dequeue())
print(q.front())
print(q.isEmpty())