import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.heap = [1]
        self.in_heap = {1}
        self.max = 1

    def popSmallest(self):
        """
        :rtype: int
        """

        smallest = heapq.heappop(self.heap)
        self.in_heap.remove(smallest)
        self.max += 1
        heapq.heappush(self.heap, self.max)
        self.in_heap.add(self.max)
        
        #print(self.max)

        return smallest
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num <= self.max:
            length = len(self.in_heap)
            self.in_heap.add(num)

            if length != len(self.in_heap):
                heapq.heappush(self.heap, num)



obj = SmallestInfiniteSet()
param_1 = obj.popSmallest()
print(param_1)
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())

obj.addBack(1)
obj.addBack(10)
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
obj.addBack(9)
obj.addBack(1)
obj.addBack(10)
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
#obj.addBack(1)