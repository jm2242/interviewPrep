# unfinished

class Heap(object):
    def __init__(self):
        '''
        In an effort to maintain a balanced tree, we'll make a complete binary tree
        Since this means all but the last row of the tree has nodes, using a list is
        an efficient way to represent the tree.
        Keep the first element reserved to maintain a nice child property where the
        children of some element at index i are at 2*i and 2*i + 1
        '''
        self.heap = [None]

    def __str__(self):
        return str(self.heap)


    ''' insert an element val into the heap
        appending to the end of self.heap requires invocation of percUp
        to maintain the heap structure property

    '''
    def insert(self, val):
        self.heap.append(val)

        # maintain heap structure property
        self.percUp(self.size())


    def size(self):
        return len(self.heap) - 1

    # percolates the element at index i as far up the tree as necessary
    # to maintain the heap structure property
    def percUp(self, i):

        while i // 2 > 0:

            # if child is less than parent
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]

                # track the original element
                i = i // 2
            else:
                break

    # pop the minimum element in the heap
    # restore the heap structure
    def popMin(self):

        # get the min element
        min_element = self.heap[1]

        # step 1 - bring up last item to the root position
        self.heap[1] = self.heap[-1]
        self.heap.pop()

        ''' step 2 - restore heap order property by swapping root with smaller of 
        children why swap with smaller of children? guaranteed to maintain heap 
        ordering wrt other child
        '''
        self.percDown(1)

        return min_element

    # percolates element at index i down, swapping with smaller of children 2*i
    # and 2*i+ 1
    def percDown(self, i):

        while (2*i + 1) <= self.size() +1:
            min_child = self.minChild(i)

            # if child is less than parent
            if self.heap[min_child] <  self.heap[i]:

                # swap elements
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
                
                # track the original element
                i = min_child
            else:
                break



    # return the index of the smaller of the children of i (either 2*i or 2*i+1)
    def minChild(self, i):

        # return the left child if there is no right child
        if 2*i + 1 > self.size():
            return 2*i

        if self.heap[2*i] < self.heap[2*i+1]:
            return 2*i
        else:
            return 2*i + 1

    # return if every element in the heap satisfies the heap ordering property
    def isOrdered(self):
        for i in range(1, self.size() // 2 + 1):
            if self.heap[i] > self.heap[2*i]: 
                return False

            # short circuit to prevent index out of range
            if 2*i+1 <= self.size() and self.heap[i] > self.heap[2*i+1]:
                return False

        else:
            return True

    '''
    build a heap from a list values
    Runtime: O(n) where n is the size of values, do to the fact percDown is used 
    instead of percUp
    '''
    def buildHeap(self, values):
        if type(values) != list:
            raise TypeError("values should be a list")
        self.heap = [None] + values
        # we won't need to worry about the second half of the list, as they should
        # all be leaves
        for i in range(len(values) // 2, 0, -1):
            self.percDown(i)

    # destructively sorts the values in the heap
    def heap_sort(self):
        return [self.popMin() for _ in range(self.size())]


def test():
    heap = Heap()
    nums = [5,10,2, 8,6,7,12]
    for x in nums:
        heap.insert(x)
    print heap.heap
    print "popped element: {0}".format( heap.popMin() )
    print heap.heap
    print heap.heap_sort()

    assert heap.isOrdered()
    newHeap = Heap()
    newHeap.buildHeap(nums)
    assert newHeap.isOrdered()
    

if __name__ == "__main__":
    test()

