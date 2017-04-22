import math
import sys

class MaxHeap:
    def __init__(self, length=100):
        self.length = length
        self.array = [0] * self.length
        self.heapsize = 0

    def parent(self, i):
        return max(0, int(math.ceil(i/2)) - 1)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def max_heapify(self, i):
        left = self.left(i)
        right = self.right(i)

        m = i
        if i < left < self.heapsize and self.array[m] < self.array[left]:
            m = left
        if i < right < self.heapsize and self.array[m] < self.array[right]:
            m = right
        if m != i:
            self.array[i], self.array[m] = self.array[m], self.array[i]
            self.max_heapify(m)

    def build_heap(self, arr):
        self.length = self.heapsize = len(arr)
        self.array = arr[:]
        for i in range(self.parent(self.heapsize-1), -1, -1):
            self.max_heapify(i)

    ### priority queue ops
    def increase_key(self, i, k):
        if self.array[i] > k:
            print("error: new key is smaller than old key")
            return
        self.array[i] = k
        while self.array[self.parent(i)] < self.array[i]:
            p = self.parent(i)
            self.array[p], self.array[i] = self.array[i], self.array[p]
            i = p

    def insert(self, x):
        if self.heapsize == self.length:
            self.array.extend([0] * self.length)
            self.length *= 2
        self.array[self.heapsize] = -2 ** 32 - 1
        self.heapsize += 1
        self.increase_key(self.heapsize-1, x)

    def maximum(self):
        return self.array[0]

    def extract_max(self):
        if self.heapsize < 1:
            print("error: heap size is 0")
            return -1
        ret = self.array[0]
        self.array[0] = self.array[self.heapsize-1]
        self.heapsize -= 1
        self.max_heapify(0)
        return ret

    def __repr__(self):
        return str(self.array[:self.heapsize])

def heap_sort(A):
    heap = MaxHeap()
    heap.build_heap(A)
    for i in range(max(0, heap.heapsize-1)):
        heap.array[0], heap.array[heap.heapsize-1] = heap.array[heap.heapsize-1], heap.array[0]
        heap.heapsize -= 1
        heap.max_heapify(0)
    return heap.array[:len(A)]

def main():
    l = [4,1,2,100,-55,-50,10,10]
    print('{} ==> {}'.format(l, heap_sort(l)))

    heap = MaxHeap()
    heap.build_heap(l)
    print('heap = {}'.format(heap))

    n1 = heap.extract_max()
    print('n1 = {}'.format(n1))
    n2 = heap.extract_max()
    print('n2 = {}'.format(n2))
    n3 = heap.extract_max()
    print('n3 = {}'.format(n3))

    heap.insert(n1 - n2)
    print('heap = {}'.format(heap))


if __name__ == '__main__':
    main()
